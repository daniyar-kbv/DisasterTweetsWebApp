from django.shortcuts import render
from django.http import JsonResponse
from utils import model, pre_processing


def home(request):
    return render(request, 'index.html')


def send_text(request):
    text = request.GET.get('text', '')
    cleaned_text = pre_processing.clean(text)
    is_disaster = model.predict(cleaned_text)
    return JsonResponse({
        'is_disaster': bool(is_disaster)
    })
