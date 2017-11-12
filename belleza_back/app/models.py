# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Estructura(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'estructura'
        verbose_name = 'Estructura'

    def __unicode__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'modalidad'

    def __unicode__(self):
        return self.nombre


class Accion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'accion'

class Nivel(models.Model):
    nombre = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nivel'

    def __unicode__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'grupo'

    def __unicode__(self):
        return self.nombre

class Subgrupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'subgrupo'

    def __unicode__(self):
        return self.nombre

class TipoAgente(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'tipo_agente'
        verbose_name = 'Tipos de Agente'

    def __unicode__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'

    def __unicode__(self):
        return self.nombre

class Agente(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.FileField(upload_to='static',blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'agente'
        verbose_name = 'Agente'

    def __unicode__(self):

        if self.user:
            return self.user.first_name
        else:
            return 'No tiene nombre'
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)



class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    #last_login = models.DateTimeField(blank=True, null=True)
    #is_superuser = models.IntegerField()
    last_name = models.CharField(max_length=30)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    nacimiento = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField('Correo personal',max_length=254,blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel', blank=True, null=True)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo', blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='grupo', blank=True, null=True)
    subgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='subgrupo', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    contacto = models.CharField(max_length=1000, blank=True, null=True)
    relacion = models.CharField('Relacion del contacto',max_length=1000, blank=True, null=True)
    movil_contacto = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.FileField(upload_to='static',blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'auth_user'
        verbose_name = 'Datos de los Usuario'

    def __unicode__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Semanas(models.Model):
    numero = models.CharField(max_length=1000)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin =  models.DateTimeField(blank=True, null=True)
    anio = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'semanas'
        verbose_name = 'Semana'

    def __unicode__(self):
        return self.numero

class Archivo(models.Model):
    ruta = models.FileField(upload_to='static',max_length=100000)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='usuario')
    nombre =  models.CharField(blank=True, null=True,max_length=10000)

    class Meta:
        managed = True
        db_table = 'archivos'
        verbose_name = 'Biblioteca'

    def __unicode__(self):
        return self.nombre

class Citas(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateTimeField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.CharField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad')
    prima_anual = models.CharField(max_length=1000,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'citas'
        verbose_name = 'Cita'


class Cliente(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='estado_civil', blank=True, null=True)
    numero_hijos = models.IntegerField()
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo')

    class Meta:
        managed = True
        db_table = 'cliente'
        verbose_name = 'Cliente'

    def __unicode__(self):
        return self.user.username


class Compania(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compania'
        verbose_name = 'Compania'

    def __unicode__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'equipo'
        verbose_name = 'Equipo'

    def __unicode__(self):
        return self.nombre

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'




class Pais(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pais'
        verbose_name = 'Paise'

    def __unicode__(self):
        return self.nombre


class Relacion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'relacion'


    def __unicode__(self):
        return self.nombre


class ParientesCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    nombre = models.CharField(max_length=1000)
    edad = models.IntegerField(blank=True,null=True)
    fecha_nacimiento =models.DateTimeField(blank=True,null=True)
    relacion = models.ForeignKey('Relacion', models.DO_NOTHING, db_column='relacion', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parientes_cliente'
        verbose_name = 'Parientes del Cliente'


class Producto(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'producto'
        verbose_name = 'Producto'

    def __unicode__(self):
        return self.nombre




class Ramo(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'ramo'

    def __unicode__(self):
        return self.nombre

class RamoCompaniaProducto(models.Model):
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo')
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto')

    class Meta:
        managed = True
        db_table = 'ramo_compania_producto'

    def __unicode__(self):
        return self.ramo.nombre+' / '+self.compania.nombre+' / '+self.producto.nombre


class PropuestaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente')
    observacion = models.CharField(max_length=10000)
    fecha = models.DateTimeField()
    detalle = models.CharField(max_length=1000)
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto')
    inforce = models.BooleanField()
    class Meta:
        managed = True
        db_table = 'propuesta_cliente'

    def __unicode__(self):
        return self.ramo_compania_producto.ramo.nombre+' / '+self.ramo_compania_producto.compania.nombre+' / '+self.ramo_compania_producto.producto.nombre



class TelefonoUser(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    numero = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'telefono_user'
        verbose_name = 'Telefonos del Usuario'



class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'estado'

    def __unicode__(self):
        return self.nombre

class Log(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user')
    accion = models.ForeignKey(Accion, models.DO_NOTHING, db_column='accion')
    detalle = models.CharField(max_length=1100)

    class Meta:
        managed = True
        db_table = 'log'



class TipoCita(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'tipo_cita'
        verbose_name = 'Tipos de Cita'

    def __unicode__(self):
        return self.nombre


class TipoSeguimiento(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'tipo_seguimiento'
        verbose_name = 'Tipos de Seguimiento'

    def __unicode__(self):
        return self.nombre

class Agentecliente(models.Model):
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente')
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        managed = True
        db_table = 'agentecliente'

class Iconos(models.Model):
    nombre = models.CharField(max_length=10000, blank=True, null=True)
    icono = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'iconos'
        verbose_name = 'Icono'

    def __unicode__(self):
        return self.nombre