from django.db import models
from django.db import models
from django.utils import timezone


class Bodega(models.Model):

    descripcion = models.CharField(max_length=100)



class Categoria(models.Model):

    descripcion = models.CharField(max_length=100)


class Moneda(models.Model):

    descripcion = models.CharField(max_length=100, default='DEFAULT VALUE')

class Productos(models.Model):
    cod_prod = models.IntegerField()
    descripcion = models.CharField(max_length=100, default='DESCRIPCION DEL PRODUCTO')
    marca = models.CharField(max_length=100, default='MARCA')
    modelo = models.CharField(max_length=100, default='MODELO')
    pr_csto = models.IntegerField()
    pr_vta = models.IntegerField()
    iva = models.IntegerField()
    cod_barra = models.IntegerField()
    stock_vta = models.IntegerField()
    stock_dev = models.IntegerField()
    fec_adq = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="productos", null = True)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Prod_Prov(models.Model):
    cod_prod = models.IntegerField()
    descripcion = models.CharField(max_length=100, default='DESCRIPCION DEL PRODUCTO')
    marca = models.CharField(max_length=100, default='MARCA')
    modelo = models.CharField(max_length=100, default='MODELO')
    pr_csto_clp = models.IntegerField()
    pr_csto_intr = models.IntegerField()
    iva = models.IntegerField()
    cod_barra = models.IntegerField()
    stock_vta = models.IntegerField()
    stock_dev = models.IntegerField()
    n_lote = models.IntegerField()
    an_lote = models.IntegerField()
    al_lote = models.IntegerField()
    pr_lote = models.IntegerField()
    imagen = models.ImageField(upload_to="prod_prov", null=True)
    fec_adq = models.DateTimeField(auto_now_add=True)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)



    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.descripcion


# Create your models here.
