# Generated by Django 3.2.3 on 2021-07-09 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bodega', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bodega_prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bodega', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_prod', models.BigIntegerField()),
                ('descripcion', models.CharField(default='DESCRIPCION DEL PRODUCTO', max_length=120)),
                ('pr_vta', models.IntegerField()),
                ('stock_vta', models.IntegerField()),
                ('stock_dev', models.IntegerField()),
                ('fec_adq', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudrest.bodega')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudrest.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Prod_Prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_prod', models.BigIntegerField()),
                ('descripcion', models.CharField(default='DESCRIPCION DEL PRODUCTO', max_length=120)),
                ('pr_costo', models.IntegerField()),
                ('stock_vta', models.IntegerField()),
                ('stock_dev', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='prod_prov')),
                ('fec_adq', models.DateTimeField(auto_now_add=True)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudrest.bodega_prov')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudrest.categoria_prov')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]
