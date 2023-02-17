from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_app.models import Todo


def index(request):
    return HttpResponse("<h1>Django REST API using docker</h1>"
                        "<p>"
                        "<a href='http://127.0.0.1:8000/todo'>TODO API</a>"
                        "<p>")


# Create your views here.
class TodoView(APIView):
    def post(self, request):
        data = request.data
        todo = Todo(task=data['task'], completed=data['completed'])
        todo.save()
        return Response(200)

    def get(self, request):
        data_list = list(Todo.objects.values())
        return Response(data_list)
