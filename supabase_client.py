import os
from supabase import create_client, Client
from django.conf import settings

url: str = settings.SUPABASE_URL
key: str = settings.SUPABASE_KEY
supabase: Client = create_client(url, key)
