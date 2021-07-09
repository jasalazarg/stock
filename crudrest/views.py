from django.shortcuts import render
from rest_framework.response import Response
from .models import Categoria, Productos,Bodega,Prod_Prov,Bodega_prov,Categoria_prov
from .serializers import ProductosSerializer,Prod_ProvSerializer,CategoriaSerializer,CategoriaProvSerializer
from rest_framework.decorators import api_view
# Create your views here.


#productos de local

@api_view(['GET'])
def ProductosLista(request):
    productos = Productos.objects.all()
    serializer = ProductosSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductosDetalle(request, pk):
    productos = Productos.objects.get(id=pk)
    serializer = ProductosSerializer(productos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ProductosCrear(request):
    serializer = ProductosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def ProductosActualizar(request, pk):
    productos = Productos.objects.get(id=pk)
    serializer = ProductosSerializer(instance=productos, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def ProductosEliminar(request, pk):
    productos = Productos.objects.get(id=pk)
    productos.delete()

    return Response('Eliminado')

#productos de proveedor
@api_view(['GET'])
def Prod_ProvLista(request):
    prod_prov = Prod_Prov.objects.all()
    serializer = Prod_ProvSerializer(prod_prov, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Prod_ProvDetalle(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    serializer = Prod_ProvSerializer(prod_prov, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def Prod_ProvCrear(request):
    serializer = Prod_ProvSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def Prod_ProvActualizar(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    serializer = Prod_ProvSerializer(instance=prod_prov, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Prod_ProvEliminar(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    prod_prov.delete()

    return Response('Eliminado')


#categorias para ventas 
@api_view(['GET'])
def Cat_Lista(request):
    categoria = Categoria.objects.all()
    serializer = CategoriaSerializer(categoria, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Cat_Detalle(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(categoria, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def Cat_Crear(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def Cat_Actualizar(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(instance=categoria, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Cat_Eliminar(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()

    return Response('Eliminado')

#productos de proveedor
@api_view(['GET'])
def Prod_ProvLista(request):
    prod_prov = Prod_Prov.objects.all()
    serializer = Prod_ProvSerializer(prod_prov, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Prod_ProvDetalle(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    serializer = Prod_ProvSerializer(prod_prov, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def Prod_ProvCrear(request):
    serializer = Prod_ProvSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def Prod_ProvActualizar(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    serializer = Prod_ProvSerializer(instance=prod_prov, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Prod_ProvEliminar(request, pk):
    prod_prov = Prod_Prov.objects.get(id=pk)
    prod_prov.delete()

    return Response('Eliminado')


#categorias para el proveedor 
@api_view(['GET'])
def CatP_Lista(request):
    cat_prov = Categoria_prov.objects.all()
    serializer = CategoriaProvSerializer(cat_prov, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CatP_Detalle(request, pk):
    cat_prov = Categoria_prov.objects.get(id=pk)
    serializer = CategoriaProvSerializer(cat_prov, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def CatP_Crear(request):
    serializer = CategoriaProvSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def CatP_Actualizar(request, pk):
    cat_prov = Categoria_prov.objects.get(id=pk)
    serializer = CategoriaProvSerializer(instance=cat_prov, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def CatP_Eliminar(request, pk):
    cat_prov = Categoria_prov.objects.get(id=pk)
    cat_prov.delete()

    return Response('Eliminado')