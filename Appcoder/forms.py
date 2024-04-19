from django import forms
from Appcoder.models import Curso, Estudiante, Profesor, Publicaciones
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EstudianteForm(forms.Form):
    nombre= forms.CharField (max_length=35)
    apellido= forms.CharField (max_length= 35)
    email= forms.EmailField ()
    dni= forms.CharField (max_length= 10)
    password= forms.CharField (max_length=30)
    

class CursoForm(forms.Form):
    nombre= forms.CharField (max_length= 35)
    promocion= forms.IntegerField ()
    
        
        

class ProfesorForm(forms.Form):
    nombre= forms.CharField (max_length= 35)
    apellido= forms.CharField (max_length= 35)
    email= forms.CharField (max_length= 35)
    especialidad= forms.CharField (max_length= 35)
       

class PublicacionesForm(forms.Form):
    titulo= forms.CharField (max_length=35)
    autor=forms.CharField (max_length= 35)
    materia= forms.CharField (max_length=35)

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}
