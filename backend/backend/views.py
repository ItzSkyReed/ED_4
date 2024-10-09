import json
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, StreamingHttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import MarkJSON
from .utils import write_to_data, get_data_json


@api_view(['POST'])
def get_user_json(request: WSGIRequest):
    if not request.body:
        return Response({'error': 'Пустое тело запроса'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        mark_data = json.loads(request.body)
    except json.JSONDecodeError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Некорректный JSON'})

    response: Response = MarkJSON.validate(mark_data)
    if response.status_code == status.HTTP_200_OK:
        write_to_data(mark_data)
    return response


@api_view(['POST'])
def get_json_file(request: WSGIRequest):
    if 'file' not in request.FILES:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Файл не найден'})
    json_file = request.FILES['file']

    try:
        mark_data = json.load(json_file)
    except json.JSONDecodeError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Некорректный JSON в файле'})

    response: Response = MarkJSON.validate(mark_data)
    if response.status_code == status.HTTP_200_OK:
        write_to_data(mark_data)
    return response


@api_view(['GET'])
def get_data(request: WSGIRequest):
    result = get_data_json()
    response = StreamingHttpResponse(result, content_type='application/json', status=status.HTTP_200_OK)

    # Устанавливаем заголовок Content-Disposition для загрузки файла
    response['Content-Disposition'] = f'attachment; filename="data.json"'

    return response
