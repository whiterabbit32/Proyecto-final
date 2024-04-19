from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns= [
   
    path ("", views.home, name= "principal"),
    path ("", views.inicio, name= "home"),
    path ("cursos", views.alta_curso, name="cursos" ),
    path ("ver_cursos", views.ver_cursos, name= "ver_cursos"),
    path ("profesor", views.profesor, name= "profesor"),
    path ("ver_profesores", views.ver_profesores, name= "ver_profesores"),
    path("edicion_profesor/<int:id>", views.editar_profesor, name="edicion_profesor"),
    path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor"),
    path ("alumnos", views.registro, name= "alumnos"),
    path ("ver_alumnos", views.ver_alumnos, name= "ver_alumnos"),
    path ("edicion_alumno/<int:id>", views.editar_alumnos, name= "edicion_alumno"),
    path ("registrar_estudiante", views.registrar_estudiante, name= "registrar estudiante"),
    path ("eliminar_alumno/ <int:id>", views.eliminar_alumno, name= "eliminar_alumno"),
    path ("ver_buscar_publicaciones", views.ver_buscar_publicaciones, name= "ver_buscar_publicaciones"),
    path ("publicacion", views.nuevas_publicaciones, name= "publicacion"),
    path ("buscar_publicaciones", views.buscar_publicaciones),
    path ("eliminar_curso/<int:id>", views.eliminar_curso, name= "eliminar_curso"),
    path ("editar_curso/ <int:id>", views.editar_curso , name= "editar_curso"),
    path ("login", views.login_request, name="login"),
    path ("inicio", views.inicio, name="inicio" ),
    path ("logout", LogoutView.as_view (template_name= "logout.html"), name= "logout"),
    path ("editar_usuario", views.editar_usuario, name= "editar_usuario")
]