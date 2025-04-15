from django.urls import path
from . import consumers  # správný import z lokálního balíčku

websocket_urlpatterns = [
    path('ws/chat/<slug:room_slug>/', consumers.ChatConsumer.as_asgi()),
]
