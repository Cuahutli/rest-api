import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from .mixins import CSRFExemptMixin

# Creating, Updating, Deleting, Retrieving(1) --Update Model
class UpdateModelDetailAPIView(CSRFExemptMixin, View):
    """
        Detail (Retrieve), Update, Delete --> Object
    """
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")


class UpdateModelListAPIView(CSRFExemptMixin, View):
    """
        List View
        Create View
    """
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "datos no encontrados"})
        return HttpResponse(data, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "No puedes borrar la lista completa"})
        return HttpResponse(data, content_type="application/json")

