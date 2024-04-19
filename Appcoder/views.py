from django.shortcuts import render, redirect
from Appcoder.models import Curso, Profesor , Publicaciones, Estudiante, Avatar
from Appcoder.forms import EstudianteForm, ProfesorForm, PublicacionesForm, CursoForm, UserEditForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def home (request):
    return render (request, "padre.html")
def inicio (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render (request , "inicio.html", {"url":avatares[0].imagen.url})
@login_required
def ver_cursos (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    cursos= Curso.objects.all()
    return render ( request, "ver_cursos.html", {"cursos": cursos,"url":avatares[0].imagen.url})

@login_required
def alta_curso (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = CursoForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_curso= Curso ( nombre= datos["nombre"], promocion= datos["promocion"])
            nuevo_curso.save()
            respuesta= loader.get_template ("cursos.html")
            mensaje= "El curso ha sido agregado con exito a la base de datos"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
         return render(request, 'cursos.html',{"url":avatares[0].imagen.url})

@login_required
def eliminar_curso (request, id):
    avatares= Avatar.objects.filter(user=request.user.id)
    curso= Curso.objects.get (id=id)
    curso.delete()
    curso= Curso.objects.all()
    mensaje= "El curso ha sido eliminado con exito de la base de datos"
    template= loader.get_template ("cursos.html")
    diccionario= {"cursos": [curso] ,"mensaje": [mensaje]}
    
    return HttpResponse (template.render(diccionario, request))
    

def editar_curso (request , id):
    avatares= Avatar.objects.filter(user=request.user.id)
    curso= Curso.objects.get (id=id)
    if request.method =="POST":
        mi_formulario= CursoForm (request.POST)
        if mi_formulario.is_valid ():
            datos= mi_formulario.cleaned_data
            curso.nombre= datos ["nombre"]
            curso.promocion= datos ["promocion"]
            curso.save()
            respuesta= loader.get_template ("cursos.html")
            mensaje= "El curso ha sido editado con exito en la base de datos"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
        mi_formulario = CursoForm(initial= {"curso": curso.nombre,"promocion": curso.promocion})
    return render (request , "editar_curso.html", {"url":avatares[0].imagen.url, "mi_formulario": mi_formulario, "curso": curso})

   








def ver_alumnos (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    alumnos= Estudiante.objects.all()
    return render ( request, "ver_alumnos.html", {"url":avatares[0].imagen.url, "alumnos": alumnos})



def registrar_estudiante(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = EstudianteForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_estudiante= Estudiante(nombre= datos["nombre"], apellido= datos["apellido"], email= datos["email"], dni= datos ["dni"])
            nuevo_estudiante.save()
            email = datos['email']
            password = datos['password']
            nuevo_usuario = User.objects.create_user(username=email, email=email, password=password)
            respuesta= loader.get_template ("alumnos.html")
            mensaje= f" Bienvenido, ha sido registrado como alumno exitosamente"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
        else:
            return HttpResponse ("formulario invalido")
    else:
        avatares= Avatar.objects.filter(user=request.user.id)
        return render(request, 'alumnos.html',{"url":avatares[0].imagen.url})
    
def editar_alumnos (request, id):
    avatares= Avatar.objects.filter(user=request.user.id)
    estudiante= Estudiante.objects.get( id=id)
    if request.method == "POST":
        mi_formulario= EstudianteForm (request.POST)
        if mi_formulario.is_valid ():
            datos= mi_formulario.cleaned_data
            estudiante.nombre= datos ["nombre"]
            estudiante.apellido= datos ["apellido"]
            estudiante.email= datos ["email"]
            estudiante.dni= datos ["dni"]
            estudiante.save()
            respuesta= loader.get_template ("alumnos.html")
            mensaje= "El alumno ha sido editado con exito en la base de datos"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
        mi_formulario = EstudianteForm(initial= {"nombre": estudiante.nombre,"apellido": estudiante.apellido, "email": estudiante.email, "dni": estudiante.dni})
    return render (request , "edicion_alumno.html", {"url":avatares[0].imagen.url,"mi_formulario": mi_formulario, "estudiante": estudiante})

def eliminar_alumno(request, id):
    avatares= Avatar.objects.filter(user=request.user.id)
    alumno= Estudiante.objects.get (id=id)
    alumno.delete()
    alumno= Estudiante.objects.all()
    mensaje= "El alumno ha sido eliminado de la base de datos"
    template= loader.get_template ("alumnos.html")
    diccionario= {"alumnos": [alumno] ,"mensaje": [mensaje]}
    
    return HttpResponse (template.render(diccionario, request))



def profesor (request):
     avatares= Avatar.objects.filter(user=request.user.id)
     if request.method == 'POST':
        form = ProfesorForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_Profe= Profesor( nombre= datos["nombre"], apellido= datos["apellido"], email= datos["email"], especialidad= datos ["especialidad"])
            nuevo_Profe.save()
            respuesta= loader.get_template ("profesores.html")
            mensaje= "el profesor ha sido registrado con éxito"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            
            return HttpResponse (documento)
     else:
         return render(request, 'profesores.html',{"url":avatares[0].imagen.url})
@login_required    
def ver_profesores (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    profesores= Profesor.objects.all()
    return render ( request, "ver_profesores.html", {"url":avatares[0].imagen.url, "profesores":profesores})

def editar_profesor (request, id):
    avatares= Avatar.objects.filter(user=request.user.id)
    profesor= Profesor.objects.get( id=id)
    if request.method == "POST":
        mi_formulario= ProfesorForm (request.POST)
        if mi_formulario.is_valid ():
            datos= mi_formulario.cleaned_data
            profesor.nombre= datos ["nombre"]
            profesor.apellido= datos ["apellido"]
            profesor.email= datos ["email"]
            profesor.especialidad= datos ["especialidad"]
            profesor.save()
            respuesta= loader.get_template ("profesores.html")
            mensaje= "El profesor ha sido editado con exito en la base de datos"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
        mi_formulario = ProfesorForm(initial= {"nombre": profesor.nombre,"apellido": profesor.apellido, "email": profesor.email, "especialidad": profesor.especialidad})
    return render (request , "edicion_profesor.html", {"url":avatares[0].imagen.url,"mi_formulario": mi_formulario, "profesor": profesor})
    
def eliminar_profesor (request, id):
    avatares= Avatar.objects.filter(user=request.user.id)
    profesor= Profesor.objects.get (id=id)
    profesor.delete()
    profesor= Profesor.objects.all()
    mensaje= "El profesor ha sido eliminado de la base de datos"
    template= loader.get_template ("profesores.html")
    diccionario= {"profesor": [profesor] ,"mensaje": [mensaje]}
    
    return HttpResponse (template.render(diccionario, request))

def ver_buscar_publicaciones (request):
    avatares= Avatar.objects.filter(user=request.user.id)
    
    return render(request, 'busqueda_publicacion.html', {"url":avatares[0].imagen.url})

def buscar_publicaciones (request):
    if request.GET ["materia"]:
        avatares= Avatar.objects.filter(user=request.user.id)
        materia= request.GET ["materia"]
        resultados= Publicaciones.objects.filter (materia__icontains= materia)
        return render (request, "resultado_busqueda.html", {"url":avatares[0].imagen.url,"publicaciones": resultados} )

def registro (request):
    return render (request, "alumnos.html")

def nuevas_publicaciones (request):
     
     if request.method == 'POST':
        form = PublicacionesForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nueva_publicacion= Publicaciones( titulo= datos["titulo"], autor= datos["autor"], materia= datos["materia"])
            nueva_publicacion.save()
            respuesta= loader.get_template ("publicacion.html")
            mensaje= f" el artículo ha sido registrado con éxito"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
     else:
         avatares= Avatar.objects.filter(user=request.user.id)
         return render(request, 'publicacion.html', {"url":avatares[0].imagen.url}) 

    
def login_request (request):
    
    if request.method=="POST":
        form= AuthenticationForm (request, data= request.POST)
        if form.is_valid ():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login (request, user)
                avatares= Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html", {"url":avatares[0].imagen.url,"mensaje": f"Bienvenido/a {username}", "usuario":username})
            else:
                return HttpResponse ("usuario no encontrado")
        else:
            return HttpResponse ("usuario no encontrado")
    else:
        avatares= Avatar.objects.filter(user=request.user.id)
        form= AuthenticationForm ()
        return render (request, "login.html", {"form":form})
    




@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            usuario.email = info ["email"]
            password= info["password1"]
            usuario.set_password (password)
            usuario.save()
            return render (request, "inicio.html")


        

    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})

    

    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


