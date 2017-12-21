from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update


#def detail_view(request):
    #return render(request, template, {}) #return JSON data --> JS Object Notation
    #return HttpResponse(get_template().render({}))

def update_model_detail_view(request):
    """
        URI -- para una API REST
    """
    data = {
        "count": 1000,
        "content": "Un nuevo contenido",
    }

    return JsonResponse(data)

