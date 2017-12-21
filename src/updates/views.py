import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update


#def detail_view(request):
    #return render(request, template, {}) #return JSON data --> JS Object Notation
    #return HttpResponse(get_template().render({}))

def json_example_view(request):
    """
        URI -- para una API REST
        GET -- Retrieve
    """
    data = {
        "count": 1000,
        "content": "Un nuevo contenido",
    }
    json_data = json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data, content_type="application/json")

