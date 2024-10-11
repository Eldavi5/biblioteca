from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def contar_palabras(request):
    archivo = request.FILES.get('archivo')
    if not archivo:
        return Response({'error': 'No se ha proporcionado ningún archivo'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        texto = archivo.read().decode('utf-8')
        palabras = texto.split()
        return Response({'cantidad_palabras': len(palabras)}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def ordenar_lista(request):
    lista_numeros = request.data.get('lista_numeros', [])
    ordenada = sorted(lista_numeros)
    return Response({'lista_ordenada': ordenada}, status=status.HTTP_200_OK)
