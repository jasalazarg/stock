from rest_framework import serializers
from .models import Categoria, Productos,Bodega,Prod_Prov,Bodega_prov,Categoria_prov



class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
        
        

class Prod_ProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod_Prov
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class BodegaProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega_prov
        fields = '__all__'

class CategoriaProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_prov
        fields = '__all__'

