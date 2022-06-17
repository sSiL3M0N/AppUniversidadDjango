from django.urls import path,include
from .views import CursoListView,eliminar_Curso
urlpatterns=[
    path('', CursoListView.as_view()),
    path('eliminarCurso/<int:id>', eliminar_Curso)
]