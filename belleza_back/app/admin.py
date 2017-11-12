from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from PIL import Image
from resizeimage import resizeimage
import os.path


from django.contrib import admin

# Register your models here.



@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','ruta')
    list_editable = ('nombre',)

@admin.register(Estructura)
class EstructuraAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion')
    list_editable = ('nombre',)

@admin.register(TipoAgente)
class TipoAgenteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Subgrupo)
class SubgrupoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Compania)
class CompaniaAgenteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Ramo)
class RamoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(TipoCita)
class TipoCitaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(TipoSeguimiento)
class TipoSeguimientoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Relacion)
class RelacionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_editable = ('nombre',)

@admin.register(Semanas)
class SemanasAdmin(admin.ModelAdmin):
    list_display = ('id','numero','fecha_inicio','fecha_fin','anio')



@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','get_estructura','get_user','get_tipo_agente','meta_personal','meta_requerida','fecha_ingreso','correo_capital','photo')
	list_editable = ('meta_personal',)


	def save_model(self, request, obj, form, change):
		
		super(AgenteAdmin, self).save_model(request, obj, form, change)
		

		# caption = '/home/capital_back/'+str(Agente.objects.get(id=obj.id).photo)
		# fd_img = open(caption, 'r')
		# img = Image.open(fd_img)
		# width, height = img.size
		# img = resizeimage.resize_cover(img, [300, 300])
		# img.save(caption, img.format)
		# fd_img.close()
	
	def get_user(self, obj):

		if obj.user:
			return obj.user.username
		else:
			return ''

	def get_tipo_agente(self, obj):

		if obj.tipo_agente:
			return obj.tipo_agente.nombre
		else:
			return ''
	def get_estructura(self, obj):
		
		if obj.estructura:
			return obj.estructura.nombre
		else:
			return ''


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','get_user','fecha_inicio','estado_civil','numero_hijos')
	list_editable = ('estado_civil',)

	def get_user(self, obj):
		return obj.user.username

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
	list_display = ('id','get_cliente','get_agente','get_tipo_cita','get_propuesta_cliente','get_tipo_seguimiento','fecha_cita','fecha_creacion','prima_target','inforce')
	list_filter = ('tipo_seguimiento__nombre','tipo_cita__nombre','agente__user__username')
	list_editable = ('inforce',)

	def get_agente(self, obj):
		return obj.agente.user.first_name

	def get_tipo_cita(self, obj):
		return obj.tipo_cita.nombre

	def get_cliente(self, obj):
		return obj.cliente.user.first_name


	def get_propuesta_cliente(self, obj):
		return obj.propuesta_cliente.ramo_compania_producto.ramo.nombre

	def get_tipo_seguimiento(self, obj):
		return obj.tipo_seguimiento.nombre




@admin.register(ParientesCliente)
class ParientesClienteAdmin(admin.ModelAdmin):
	list_display = ('id','get_cliente','nombre','edad','relacion')
	

	def get_cliente(self, obj):
		return obj.cliente.user.username


@admin.register(PropuestaCliente)
class PropuestaClienteAdmin(admin.ModelAdmin):
	list_display = ('id','get_cliente','get_agente','get_ramo','observacion','fecha','detalle','inforce')
	list_editable = ('inforce',)
	
	def get_cliente(self, obj):
		return obj.cliente.user.username

	def get_agente(self, obj):
		return obj.agente.user.username

	def get_ramo(self, obj):
		return obj.ramo_compania_producto.ramo.nombre + ' / ' + obj.ramo_compania_producto.compania.nombre +' / '+obj.ramo_compania_producto.producto.nombre

@admin.register(RamoCompaniaProducto)
class RamoCompaniaProductoAdmin(admin.ModelAdmin):
	list_display = ('id','get_ramo','get_compania','get_producto')
	
	def get_ramo(self, obj):
		return obj.ramo.nombre

	def get_compania(self, obj):
		return obj.compania.nombre

	def get_producto(self, obj):
		return obj.producto.nombre


# class DatosInline(admin.StackedInline):
#     model = DatosUsuario
#     can_delete = False


# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (DatosInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)



@admin.register(TelefonoUser)
class TelefonoUserAdmin(admin.ModelAdmin):
	list_display = ('id','get_user','numero')
	
	def get_user(self, obj):
		return obj.user.username


@admin.register(Iconos)
class IconosAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','icono')
	



@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
	list_display = ('id','pais','get_equipo','username','first_name','last_name','get_nivel','get_grupo','get_subgrupo','correo_capital','email','nacimiento','telefono','direccion','dni','contacto','relacion','movil_contacto','fecha_ingreso')
	#list_editable = ('email',)
	search_fields = ('first_name',)
	list_filter = ('nivel__nombre','equipo__nombre')





	def save_model(self, request, obj, form, change):



		if Agente.objects.filter(user_id=obj.id):

			age_obj = Agente.objects.get(user_id=obj.id)
			age_obj.equipo=obj.equipo
			age_obj.tipo_agente_id=obj.tipo_agente
			age_obj.meta_personal=obj.meta_personal
			age_obj.meta_requerida=obj.meta_requerida
			age_obj.fecha_ingreso=obj.fecha_ingreso
			age_obj.correo_capital=obj.correo_capital
			age_obj.photo=obj.photo
			age_obj.save()

		else:

			print 'nivel',obj.nivel

			if obj.nivel:

				if obj.nivel.nombre!='Cliente':


					if obj.tipo_agente:

						id_tipo_agente = obj.tipo_agente.id

					else:

						id_tipo_agente = None


					Agente(photo=obj.photo,user_id=obj.id,tipo_agente_id=id_tipo_agente,meta_requerida=obj.meta_requerida,meta_personal=obj.meta_requerida,fecha_ingreso=obj.fecha_ingreso,correo_capital=obj.correo_capital,equipo=obj.equipo).save()

		super(AuthUserAdmin, self).save_model(request, obj, form, change)

		caption = '/home/capital_back/'+str(AuthUser.objects.get(id=obj.id).photo)

		if os.path.isfile(caption):
		
			fd_img = open(caption, 'r')
			img = Image.open(fd_img)
			width, height = img.size
			img = resizeimage.resize_cover(img, [300, 300])
			img.save(caption, img.format)
			fd_img.close()


	def get_nivel(self, obj):

		if obj.nivel:
				return obj.nivel.nombre
		else:
				return ''
	get_nivel.short_description = 'Nivel'
	get_nivel.admin_order_field = 'equipo_id'

	def get_grupo(self, obj):

		if obj.grupo:
				return obj.grupo.nombre
		else:
				return ''
	get_grupo.short_description = 'Grupo'
	get_grupo.admin_order_field = 'equipo_id'

	def get_subgrupo(self, obj):

		if obj.subgrupo:
				return obj.subgrupo.nombre
		else:
				return ''
	get_subgrupo.short_description = 'Subgrupo'
	get_subgrupo.admin_order_field = 'equipo_id'


	def get_equipo(self, obj):

		if obj.equipo:
				return obj.equipo.nombre
		else:
				return ''

	get_equipo.short_description = 'Equipo'
	get_equipo.admin_order_field = 'equipo_id'



