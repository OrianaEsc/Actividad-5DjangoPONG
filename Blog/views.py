from django.shortcuts import render
from Blog.models import Posteo, Comentario 
from Blog.forms import FormComentario

# Create your views here.
def blog_index(request):
    #Todos los posts ordenados por el campo created_on de forma descendiente
    posteos = Posteo.objects.all().order_by('-created_on')

    context = {
        'posteos' : posteos,
    }

    return render(request, 'index.html', context) 

def blog_detail(request, pk):
    #Un post en especifico
    posteo = Posteo.objects.get(pk=pk)

    formulario = FormComentario()
    if request.method == 'POST':
        #Se requiere guardar un comentario en este post 
        formulario = FormComentario(request.POST)

        if formulario.is_valid():
            comentario = Comentario(
                autor = formulario.cleaned_data['autor'],
                body = formulario.cleaned_data['body'],
                posteo = posteo
            )
            #Guardando el comentario
            comentario.save()

            #Limpiamos los campos del formulario
            formulario = FormComentario()

    #Filtrado de los comentarios pertenecientes a este post para  mostrarlo en el templete 
    comentarios = Comentario.objects.filter(posteo = posteo)

    context = {
        'posteo': posteo,
        'comentarios': comentarios,
        'formularios': formulario
    } 

    return render(request,'detail.html', context)
