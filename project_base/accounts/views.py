from django.views.generic import View
from django.http.response import JsonResponse
from django.shortcuts import render


class IndexView(View):

    def get(self, request):
        response = JsonResponse({'data': 'spam'})
        return response
