from django.urls import path
from .import views

urlpatterns = [
    #endpoints de productos para ventas, posventa dir ip  -/endpoint xxx.xxx.xxx.x/detalle/
    path('', views.ProductosLista, name="productos"),
    path('detalle/<str:pk>', views.ProductosDetalle, name="detalle"),
    path('crear', views.ProductosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.ProductosActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.ProductosEliminar, name="eliminar"),
    
    #endpoints de categoria para venta y posventa
    path('categoria', views.Cat_Lista, name="productos"),
    path('cat_detalle/<str:pk>', views.Cat_Detalle, name="detalle"),
    path('cat_crear', views.Cat_Crear, name="crear"),
    path('cat_actualizar/<str:pk>/', views.Cat_Actualizar, name="actualizar"),
    path('cat_eliminar/<str:pk>/', views.Cat_Eliminar, name="eliminar"),
    



    #endpoints de provedores xxx.xxx.xxx.x/prod_prov/
    path('prod_prov', views.Prod_ProvLista, name="prod_Prov_Lista"),
    path('prd_p_detalle/<str:pk>', views.Prod_ProvDetalle, name="detalle"),
    path('prd_p_crear', views.Prod_ProvCrear, name="crear"),
    path('prd_p_actualizar/<str:pk>/', views.Prod_ProvActualizar, name="actualizar"),
    path('prd_p_eliminar/<str:pk>/', views.Prod_ProvEliminar, name="eliminar"),



    #endpoints de categorias para provedores xxx.xxx.xxx.x/prod_prov/
    path('categoria_prov', views.CatP_Lista, name="prod_Prov_Lista"),
    path('cat_p_detalle/<str:pk>', views.CatP_Detalle, name="detalle"),
    path('cat_p_crear', views.CatP_Crear, name="crear"),
    path('cat_p_actualizar/<str:pk>/', views.CatP_Actualizar, name="actualizar"),
    path('cat_p_eliminar/<str:pk>/', views.CatP_Eliminar, name="eliminar"),


]
