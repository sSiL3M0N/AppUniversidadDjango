from django.shortcuts import render, redirect
from .models import Curso
from django.views.generic import ListView
# Create your views here.
def home(request):
    cursoslistado = Curso.objects.all().order_by("-nombre")
    """
    #cursosListado=Curso.objects.all().order_by("id")
    cursosListado=Curso.objects.all().order_by('nombre')
    cursosListado = Curso.objects.all().order_by('-nombre')
    cursosListado = Curso.objects.all().order_by('creditos')
    cursosListado=Curso.objects.all().order_by('nombre','creditos')
    cursosListado = Curso.objects.all().filter(nombre__startswith='I')
    cursosListado=Curso.objects.all().filter(nombre__endswith='II')
    cursosListado=Curso.objects.all().filter(nombre__contains='I')
    """
    return render(request, "gestionCursos.html", {'cursoListado': cursoslistado, 'titulo': 'Gestión de MIS cursos'})
    # return HttpResponse("<p> Hola mundo </p>")

class CursoListView(ListView):

    model = Curso
    template_name = 'gestionCursos.html'

    def get_context_data(self, **kwargs):

        context=super().get_context_data()

        context['Titulo']="Gestion de cursos"

        return context

    def get_queryset(self):
        return Curso.objects.all().order_by('creditos')

def eliminar_Curso(request,id):
    Curso.objects.get(id=id).delete()

    return redirect("/")
