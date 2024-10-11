from rest_framework import viewsets
from tareas.models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
