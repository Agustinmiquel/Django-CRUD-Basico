from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    apellido = models.TextField()
    edad= models.CharField(max_length=200)
    created_at= models.DateField(auto_now_add=True)

    def str(self):
        return self.nombre
    
    class Meta:
        db_table = 'Cliente'
        verbose_name = 'cliente'
        verbose_name_plural = "Clientes"
