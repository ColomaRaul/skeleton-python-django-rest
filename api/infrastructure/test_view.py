from django.http import JsonResponse
from rest_framework import status
from django.views import View


class TestView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return JsonResponse({'message': 'test'}, status=status.HTTP_200_OK)
