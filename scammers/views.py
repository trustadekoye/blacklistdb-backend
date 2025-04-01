import requests
import os
import uuid
from rest_framework import status, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import ScammersList
from .serializers import ScammersListSerializer
from supabase_client import supabase


class NigerianBanksView(APIView):
    def get(self, request):
        try:
            # Fetch banks from the Nigerian Banks API
            response = requests.get("https://nigerianbanks.xyz")
            if response.status_code == 200:
                return Response(response.json())
            return Response(
                {"error": "Failed to fetch banks"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ScammersViewSet(viewsets.ModelViewSet):
    queryset = ScammersList.objects.filter(status="approved")
    serializer_class = ScammersListSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAdminUser])
    def all_reports(self, request):
        queryset = ScammersList.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the data
        data = request.data.copy()

        # Handle image upload
        scammers_image = request.FILES.get("scammers_image")
        if scammers_image:
            file_ext = os.path.splitext(scammers_image.name)[1]
            file_name = f"scammers_images/{uuid.uuid4()}{file_ext}"

            # Upload to Supabase Storage
            try:
                res = supabase.storage.from_("scammersdb").upload(
                    file_name, scammers_image.read()
                )
                # Get the public URL
                file_url = supabase.storage.from_("scammersdb").get_public_url(
                    file_name
                )
                data["scammers_image"] = file_url
            except Exception as e:
                return Response(
                    {"error": f"Failed to upload image: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        # Handle documents upload
        other_documents = request.FILES.get("other_documents")
        if other_documents:
            file_ext = os.path.splitext(other_documents.name)[1]
            file_name = f"scammers_documents/{uuid.uuid4()}{file_ext}"

            # Upload to Supabase Storage
            try:
                res = supabase.storage.from_("scammersdb").upload(
                    file_name, other_documents.read()
                )

                # Get the public URL
                file_url = supabase.storage.from_("scammersdb").get_public_url(
                    file_name
                )
                data["other_documents"] = file_url
            except Exception as e:
                return Response(
                    {"error": f"Failed to upload document: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        # Process the serializer with our modified data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
