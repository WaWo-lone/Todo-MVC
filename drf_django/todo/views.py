import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import TodoContent


# Create your views here.
class TodosView(View):
    def get(self, request):
        todos = TodoContent.objects.all()
        data_list = []

        for todo in todos:
            data_list.append({
                'id': todo.id,
                'contents': todo.contents,
                'ischecked': todo.ischecked,
                'isActive': todo.isActive,
                'isEditing': todo.isEditing
            })

        return JsonResponse(data_list, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        todo = TodoContent.objects.create(contents=data.get('contents'))
        data_dict = {
            'id': todo.id,
            'contents': todo.contents,
            'ischecked': todo.ischecked,
            'isActive': todo.isActive,
            'isEditing': todo.isEditing
        }
        return JsonResponse(data_dict)


class TodoView(View):
    def put(self, request, id):
        # print(id)
        todo = TodoContent.objects.filter(id=id)
        data = json.loads(request.body)
        TodoContent.objects.filter(id=id).update(contents=data.get('contents'))
        # print(data.get('contents'))
        data_dict = {
            'id': todo[0].id,
            'contents': data.get('contents'),
            'ischecked': todo[0].ischecked,
            'isActive': todo[0].isActive,
            'isEditing': todo[0].isEditing
        }
        return JsonResponse(data_dict)

    def delete(self, request, id):
        todo = TodoContent.objects.get(id=id)
        todo.delete()
        return JsonResponse({})


class TodoDelView(View):

    def post(self, request):
        data = json.loads(request.body)
        print(data)
        id_list = data.get('id_list')
        print(id_list)
        for id in id_list:
            todo = TodoContent.objects.get(id=id)
            todo.delete()
        return JsonResponse({})
