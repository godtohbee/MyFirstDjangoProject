from django.http import response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from .serializers import ArtisteSerializer
from musicapp.models import Artiste, Song, Lyric

# Create your views here
@api_view(['GET', 'POST'])
def artiste_list_api(request):
    if request.method == 'GET':
        songcrud = Artiste.objects.all()
        serializer = ArtisteSerializer(songcrud, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'ADD', 'DELETE'])
def artiste_detail_api(request, id):
    try:
        Artiste = Artiste.objects.get(id=id)
    except Artiste.DoesNotExist:
        return Response({'message':'Artiste Not Found'}, status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtisteSerializer(Artiste)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'ADD':
        serializer = ArtisteSerializer(Artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Artiste.delete()
        return Response({'message':'Artiste Deleted'}, status=HTTP_204_NO_CONTENT)
