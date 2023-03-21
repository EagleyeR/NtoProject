from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')


from lab.consumers import Consumer


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws', Consumer.as_asgi())
        ])
    )
})
