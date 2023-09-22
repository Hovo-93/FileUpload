from rest_framework import generics, status
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer, FileListSerializer
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from .task import check_processed


# Create your views here.
class FileUploadView(generics.CreateAPIView):
    """Класс для загрузки файлов"""
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # Парсеры для обработки файловых данных в запросе
    parser_classes = (FileUploadParser, FormParser, MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid(raise_exception=True):
            self.perform_create(file_serializer)

            file_instance = file_serializer.instance

            file_id = file_instance.id
            # Запуск асинхронной задачи для обработки processed с использованием Celery
            check_processed.delay(int(file_id))

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    """Класс для получения всех файлов"""
    serializer_class = FileListSerializer
    queryset = File.objects.all()
