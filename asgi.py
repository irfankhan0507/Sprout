import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

django_asgi_app = get_asgi_application()

# Import your websocket consumer here if you implement one
# from chat_app.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # "websocket": AllowedHostsOriginValidator(
    #     AuthMiddlewareStack(
    #         URLRouter([
    #             path("ws/chat/", ChatConsumer.as_asgi()),
    #         ])
    #     )
    # ),
})