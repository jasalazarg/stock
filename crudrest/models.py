
from django.db import models
from django.utils import timezone

class Bodega(models.Model):
    nom_bodega = models.CharField(max_length=100)
class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=100)
class Categoria_prov(models.Model):
    nom_categoria = models.CharField(max_length=100)
class Bodega_prov(models.Model):
    nom_bodega = models.CharField(max_length=100)
class Productos(models.Model):
    cod_prod = models.BigIntegerField()
    descripcion = models.CharField(max_length=120, default='DESCRIPCION DEL PRODUCTO')
    pr_vta = models.IntegerField()
    stock_vta = models.IntegerField()
    stock_dev = models.IntegerField()
    fec_adq = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="productos", null = True)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
class Prod_Prov(models.Model):
    cod_prod = models.BigIntegerField()
    descripcion = models.CharField(max_length=120, default='DESCRIPCION DEL PRODUCTO')
    precio = models.IntegerField()
    stock_vta = models.IntegerField()
    stock_dev = models.IntegerField()
    imagen = models.ImageField(upload_to="prod_prov", null=True)
    fec_adq = models.DateTimeField(auto_now_add=True)
    bodega = models.ForeignKey(Bodega_prov, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria_prov, on_delete=models.CASCADE)
    


    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.descripcion


