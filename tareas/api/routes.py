from rest_framework.routers import DefaultRouter
from .views import TareaViewSet

router_tareas = DefaultRouter()

router_tareas.register(
    prefix="tareas", basename="tareas", viewset=TareaViewSet
)
