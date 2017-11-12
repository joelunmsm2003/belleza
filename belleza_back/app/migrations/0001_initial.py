# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-13 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'accion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_personal', models.IntegerField(blank=True, null=True)),
                ('meta_requerida', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('correo_capital', models.CharField(blank=True, max_length=1000, null=True)),
                ('photo', models.FileField(upload_to='static')),
            ],
            options={
                'verbose_name': 'Agente',
                'db_table': 'agente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Agentecliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(db_column='agente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Agente')),
            ],
            options={
                'db_table': 'agentecliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthGroup')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('nacimiento', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True, verbose_name='Correo personal')),
                ('correo_capital', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('meta_personal', models.IntegerField(blank=True, null=True)),
                ('meta_requerida', models.IntegerField(blank=True, null=True)),
                ('dni', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono', models.CharField(blank=True, max_length=1000, null=True)),
                ('contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('relacion', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Relacion del contacto')),
                ('movil_contacto', models.CharField(blank=True, max_length=1000, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='static')),
            ],
            options={
                'verbose_name': 'Datos de los Usuario',
                'db_table': 'auth_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthPermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField()),
                ('observacion', models.CharField(max_length=10000)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('prima_target', models.CharField(max_length=1000)),
                ('prima_anual', models.CharField(max_length=1000)),
                ('fecha_poliza', models.DateTimeField()),
                ('fecha_creacion', models.DateTimeField()),
                ('agente', models.ForeignKey(db_column='agente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Agente')),
            ],
            options={
                'verbose_name': 'Cita',
                'db_table': 'citas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('numero_hijos', models.IntegerField()),
                ('agente', models.ForeignKey(db_column='agente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Agente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Compania',
                'db_table': 'compania',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'db_table': 'equipo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'estado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'db_table': 'estado_civil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estructura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Estructura',
                'db_table': 'estructura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'grupo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Iconos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=10000, null=True)),
                ('icono', models.CharField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'verbose_name': 'Icono',
                'db_table': 'iconos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=1100)),
                ('accion', models.ForeignKey(db_column='accion', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Accion')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser')),
            ],
            options={
                'db_table': 'log',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'modalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'nivel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Paise',
                'db_table': 'pais',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ParientesCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('edad', models.IntegerField()),
                ('cliente', models.ForeignKey(db_column='cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cliente')),
            ],
            options={
                'verbose_name': 'Parientes del Cliente',
                'db_table': 'parientes_cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Producto',
                'db_table': 'producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PropuestaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=10000)),
                ('fecha', models.DateTimeField()),
                ('detalle', models.CharField(max_length=1000)),
                ('agente', models.ForeignKey(db_column='agente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Agente')),
                ('cliente', models.ForeignKey(db_column='cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cliente')),
            ],
            options={
                'db_table': 'propuesta_cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'ramo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RamoCompaniaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compania', models.ForeignKey(db_column='compania', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Compania')),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Producto')),
                ('ramo', models.ForeignKey(db_column='ramo', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Ramo')),
            ],
            options={
                'db_table': 'ramo_compania_producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'relacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Semanas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=1000)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('anio', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Semana',
                'db_table': 'semanas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subgrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'subgrupo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TelefonoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser')),
            ],
            options={
                'verbose_name': 'Telefonos del Usuario',
                'db_table': 'telefono_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoAgente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Tipos de Agente',
                'db_table': 'tipo_agente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipos de Cita',
                'db_table': 'tipo_cita',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoSeguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Tipos de Seguimiento',
                'db_table': 'tipo_seguimiento',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='propuestacliente',
            name='ramo_compania_producto',
            field=models.ForeignKey(db_column='ramo_compania_producto', on_delete=django.db.models.deletion.DO_NOTHING, to='app.RamoCompaniaProducto'),
        ),
        migrations.AddField(
            model_name='parientescliente',
            name='relacion',
            field=models.ForeignKey(blank=True, db_column='relacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Relacion'),
        ),
        migrations.AlterUniqueTogether(
            name='djangocontenttype',
            unique_together=set([('app_label', 'model')]),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='equipo',
            field=models.ForeignKey(db_column='equipo', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Equipo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado_civil',
            field=models.ForeignKey(blank=True, db_column='estado_civil', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.EstadoCivil'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser'),
        ),
        migrations.AddField(
            model_name='citas',
            name='cliente',
            field=models.ForeignKey(db_column='cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cliente'),
        ),
        migrations.AddField(
            model_name='citas',
            name='modalidad',
            field=models.ForeignKey(db_column='modalidad', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Modalidad'),
        ),
        migrations.AddField(
            model_name='citas',
            name='propuesta_cliente',
            field=models.ForeignKey(db_column='propuesta_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.PropuestaCliente'),
        ),
        migrations.AddField(
            model_name='citas',
            name='semana',
            field=models.ForeignKey(db_column='semana', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Semanas'),
        ),
        migrations.AddField(
            model_name='citas',
            name='tipo_cita',
            field=models.ForeignKey(db_column='tipo_cita', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TipoCita'),
        ),
        migrations.AddField(
            model_name='citas',
            name='tipo_seguimiento',
            field=models.ForeignKey(db_column='tipo_seguimiento', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TipoSeguimiento'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='equipo',
            field=models.ForeignKey(blank=True, db_column='equipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Equipo'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='estructura',
            field=models.ForeignKey(blank=True, db_column='estructura', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Estructura'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='grupo',
            field=models.ForeignKey(blank=True, db_column='grupo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Grupo'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='nivel',
            field=models.ForeignKey(blank=True, db_column='nivel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Nivel'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='pais',
            field=models.ForeignKey(blank=True, db_column='pais', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Pais'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='subgrupo',
            field=models.ForeignKey(blank=True, db_column='subgrupo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Subgrupo'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='tipo_agente',
            field=models.ForeignKey(blank=True, db_column='tipo_agente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.TipoAgente'),
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='authgrouppermissions',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthPermission'),
        ),
        migrations.AddField(
            model_name='agentecliente',
            name='cliente',
            field=models.ForeignKey(db_column='cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cliente'),
        ),
        migrations.AddField(
            model_name='agente',
            name='equipo',
            field=models.ForeignKey(blank=True, db_column='equipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Equipo'),
        ),
        migrations.AddField(
            model_name='agente',
            name='estructura',
            field=models.ForeignKey(blank=True, db_column='estructura', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Estructura'),
        ),
        migrations.AddField(
            model_name='agente',
            name='tipo_agente',
            field=models.ForeignKey(blank=True, db_column='tipo_agente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.TipoAgente'),
        ),
        migrations.AddField(
            model_name='agente',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.AuthUser'),
        ),
        migrations.AlterUniqueTogether(
            name='authuseruserpermissions',
            unique_together=set([('user', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='authusergroups',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='authpermission',
            unique_together=set([('content_type', 'codename')]),
        ),
        migrations.AlterUniqueTogether(
            name='authgrouppermissions',
            unique_together=set([('group', 'permission')]),
        ),
    ]