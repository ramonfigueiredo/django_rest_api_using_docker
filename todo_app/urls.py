from django.urls import path
from todo_app.views import TodoView, index

urlpatterns = [
    path('', index, name='index'),
    path('todo', TodoView.as_view())
]