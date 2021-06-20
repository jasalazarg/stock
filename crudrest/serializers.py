from rest_framework import serializers
from .models import Productos
from .models import Prod_Prov


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class Prod_ProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod_Prov
        fields = '__all__'
