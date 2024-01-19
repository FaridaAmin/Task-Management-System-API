from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDelete


urlpatterns = [
    path('TMSys',TaskListCreate.as_view(), name="Create-TMSys-List"),
    path('task/<int:pk>', TaskRetrieveUpdateDelete.as_view(), name='task-Details')
    ]