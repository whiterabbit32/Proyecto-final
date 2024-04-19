from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso (models.Model):
    nombre= models.CharField (max_length=40)
    promocion= models.IntegerField ()
    
    def __str__(self):
        return f"nombre:  {self.nombre}     promocion: {self.promocion}"
    



class Estudiante (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    email = models.EmailField()
    
    


class Profesor (models.Model):
    nombre = models.CharField (max_length= 35)
    apellido = models.CharField (max_length= 35)
    email= models.EmailField()
    especialidad= models.CharField( max_length=30)

class Publicaciones (models.Model):
    titulo= models.CharField (max_length =35)
    autor= models.CharField (max_length =35)
    materia= models.CharField (max_length =35)

class Avatar (models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE )
    imagen= models.ImageField (upload_to= "avatares", null= True, blank=True)

    def __str__(self):
        return f" usuario{self.user} ,imagen: {self.imagen}"
    
