import json
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm
from cfeapi.mixins import  HttpResponseMixin
from .mixins import CSRFExemptMixin
from .utils import is_json


# Creating, Updating, Deleting, Retrieving(1) --Update Model
class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
        Detail (Retrieve), Update, Delete --> Object
    """
    is_json = True 
    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExists:
        #     obj = None
        # return obj
        """
            El método de abajo también maneja si no existe
        """
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update nno encontrado"})
            return self.render_to_response(error_data, status=404)    
        json_data = obj.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "No permitido, por favor usa /api/updates/ para crear."})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Datos enviados son invalidos, por favor envía un JSON"})
            return self.render_to_response(error_data, status=404)    

        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update nno encontrado"})
            return self.render_to_response(error_data, status=404)      
        

        data = json.loads(obj.serialize())
        print(data)
        passed_data = json.loads(request.body.decode('utf-8'))
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        print(data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message":"something"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update nno encontrado"})
            return self.render_to_response(error_data, status=404)   

        deleted_, item_deleted = obj.delete() 
        if deleted_ == 1:
            json_data = json.dumps({"message":"Eliminado correctamente"})
            return self.render_to_response(json_data, status=200)
        
        error_data = json.dumps({"message": "No se pudo borrar el item, intentalo más tarde"})
        return self.render_to_response(error_data, status=400)   

#AUTH / Permissions --> DJANGO REST FRAMEWORK --> Don't use Tastypie
# /api/updates

class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
        List View --> Retrieve --> Detail View
        Create View
        Update
        Delete
    """
    is_json = True 
    queryset = None
    
    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs
        
    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExists:
        #     obj = None
        # return obj
        """
            El método de abajo también maneja si no existe
        """
        if id is None:
            return None

        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"message": "Objeto no encontrado"})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Datos enviados son invalidos, por favor envía un JSON"})
            return self.render_to_response(error_data, status=404)   
        
        data = json.loads(request.body.decode('utf-8'))
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({"message": "Método no permitido"})
        return self.render_to_response(data, status=400)

    # def delete(self, request, *args, **kwargs):
    #     data = json.dumps({"message": "No puedes borrar la lista completa"})
    #     status_code =  403#No Permitido
    #     return self.render_to_response(data, status=status_code)

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Datos enviados son invalidos, por favor envía un JSON"})
            return self.render_to_response(error_data, status=404)    
        passed_data = json.loads(request.body.decode('utf-8'))
        print(passed_data)
        passed_id = passed_data.get('id', None)

        if not passed_id:
            error_data = json.dumps({"id": "Esta campo es requerido para actualizar"})
            return self.render_to_response(error_data, status=404)

        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Update no encontrado"})
            return self.render_to_response(error_data, status=404)      
        

        data = json.loads(obj.serialize())
        
        
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        print(data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message":"something"})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Datos enviados son invalidos, por favor envía un JSON"})
            return self.render_to_response(error_data, status=404)    
        passed_data = json.loads(request.body.decode('utf-8'))
        passed_id = passed_data.get('id', None)

        if not passed_id:
            error_data = json.dumps({"id": "Esta campo es requerido para actualizar"})
            return self.render_to_response(error_data, status=404)

        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Update nno encontrado"})
            return self.render_to_response(error_data, status=404)  

       
        deleted_, item_deleted = obj.delete() 
        if deleted_ == 1:
            json_data = json.dumps({"message":"Eliminado correctamente"})
            return self.render_to_response(json_data, status=200)
        
        error_data = json.dumps({"message": "No se pudo borrar el item, intentalo más tarde"})
        return self.render_to_response(error_data, status=400)  

