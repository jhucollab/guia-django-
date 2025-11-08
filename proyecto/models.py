from django.db import models
#clases(models)=
#tipos= energia
class Energia(models.Model):
    tipo = models.CharField(max_length=100)
    formula = models.CharField()
    def __str__(self):
        return f"energia= {self.tipo}"
#particulas
class Particula(models.Model):
    carga_electrica = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.carga_electrica 
# Create your models here. py 