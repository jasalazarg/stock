from django.urls import path
from .import views

urlpatterns = [
    #endpoints de ventas, posventa dir ip  -/endpoint xxx.xxx.xxx.x/detalle/
    path('', views.ProductosLista, name="productos"),
    path('detalle/<str:pk>', views.ProductosDetalle, name="detalle"),
    path('crear', views.ProductosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.ProductosActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.ProductosEliminar, name="eliminar"),
    #endpoints de provedores xxx.xxx.xxx.x/prod_prov/
    path('prod_prov', views.Prod_ProvLista, name="prod_Prov_Lista"),
    path('prd_prv_detalle/<str:pk>', views.Prod_ProvDetalle, name="detalle"),
    path('prd_prv_crear', views.Prod_ProvCrear, name="crear"),
    path('prd_prv_actualizar/<str:pk>/', views.Prod_ProvActualizar, name="actualizar"),
    path('prd_prv_eliminar/<str:pk>/', views.Prod_ProvEliminar, name="eliminar"),
]


