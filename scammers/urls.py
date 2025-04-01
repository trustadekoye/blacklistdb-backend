from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScammersViewSet, NigerianBanksView

router = DefaultRouter()
router.register(r"scammers", ScammersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("nigerian-banks/", NigerianBanksView.as_view(), name="nigerian-banks"),
]
