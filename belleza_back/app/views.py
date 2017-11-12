#    ___       ___       ___       ___            ___       ___   
#   /\  \     /\__\     /\  \     /\__\          /\  \     /\  \  
#  /  \  \   / | _|_   /  \  \   |  L__L        _\ \  \   /  \  \ 
# /  \ \__\ /  |/\__\ / /\ \__\  |   \__\      /\/  \__\ / /\ \__\
# \/\  /  / \/|  /  / \ \/ /  /  /   /__/      \  /\/__/ \ \/ /  /
#   / /  /    | /  /   \  /  /   \/__/          \/__/     \  /  / 
#   \/__/     \/__/     \/__/                              \/__/

# email : joelunmsm@gmail.com
# web   : xiencias.com



from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import View
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.db.models import Count,Sum
from app.models import *
from app.serializers import *

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from django.contrib.auth import authenticate
import time
from django.db.models import Func
import os
from datetime import datetime,timedelta,date
import os.path
import requests
import smtplib
from email.mime.text import MIMEText
from django.db.models import Count,Max
import datetime
import random
from django.db.models import Count,Sum
from PIL import Image
from resizeimage import resizeimage

class Uploadphoto(JSONWebTokenAuthMixin, View):

	#Retorna datos del agente
	def post(self, request):

		caption = request.FILES['file']

		#Guarda foto

		print caption

		id_user =request.user.id

		print id_user

		a = Agente.objects.get(user_id=id_user)

		a.photo = caption
		a.save()


		caption = '/home/capital_back/'+str(Agente.objects.get(user_id=id_user).photo)

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		width, height = img.size

		img = resizeimage.resize_cover(img, [300, 300])

		img.save(caption, img.format)

		fd_img.close()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")




def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]


class Agenterest(JSONWebTokenAuthMixin, View):

	
	#Actualiza datos
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)
		telefono = None

		a = Agente.objects.get(user_id=id)

		for i in data:
            
			if i=='tipo_agente' :tipo_agente=data['tipo_agente']
			if i=='meta_personal' :a.meta_personal=data['meta_personal']
			if i=='meta_requerida' :a.meta_requerida=data['meta_requerida']
			if i=='correo_capital' :a.correo_capital=data['correo_capital']
			if i=='user__email' :email=data['user__email']
			if i=='photo' :a.photo=data['photo']
			if i=='user__direccion' :direccion=data['user__direccion']
			if i=='user__dni' :dni=data['user__dni']
			if i=='telefono':telefono=data['telefono']
			if i=='password':
				u = User.objects.get(id=id)
				u.set_password(data['password'])
				u.save()



			if i=='telefono':
				TelefonoUser(user_id=a.user.id,numero=data['telefono']).save()

	
		a.save()

		au = AuthUser.objects.get(id=id)
		au.email = email
		au.direccion = direccion
		au.dni= dni
		au.telefono=telefono
		au.save()

		a= simplejson.dumps('OK')
		return HttpResponse(a, content_type="application/json")

	#Retorna datos del agente
	def get(self, request):

		
		id =request.user.id
		a = Agente.objects.filter(user_id=id).values('user','photo','id','estructura__nombre','user__pais__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username')
		fmt = '%d %b %Y'
		for j in range(len(a)):

			if Agente.objects.get(id=a[j]['id']).fecha_ingreso:
				a[j]['fecha_ingreso'] = Agente.objects.get(id=a[j]['id']).fecha_ingreso.strftime(fmt)
			if Agente.objects.get(id=a[j]['id']).user.nacimiento:
				a[j]['fecha_nacimiento'] = Agente.objects.get(id=a[j]['id']).user.nacimiento
			if TelefonoUser.objects.filter(user_id=a[j]['user']):
				a[j]['telefono']=TelefonoUser.objects.filter(user_id=a[j]['user']).values('numero').order_by('-id')[0]['numero']

		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")


class Listacliente(JSONWebTokenAuthMixin, View):

	#Retorna datos del agente
	def get(self, request,cliente):

		id_user_cliente = Cliente.objects.get(id=cliente).user.id


		a =Cliente.objects.filter(id=cliente).values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		
		fmt = '%Y-%m-%d'
		
		for j in range(len(a)):

			if Cliente.objects.get(id=a[j]['id']).fecha_inicio: 
				a[j]['fecha_inicio'] = Cliente.objects.get(id=a[j]['id']).fecha_inicio.strftime(fmt)
			if AuthUser.objects.get(id=id_user_cliente).nacimiento:
				a[j]['fecha_nacimiento'] = AuthUser.objects.get(id=id_user_cliente).nacimiento
			if TelefonoUser.objects.filter(user_id=id_user_cliente).count()>0:
				a[j]['telefono'] = TelefonoUser.objects.filter(user_id=id_user_cliente).order_by('-id').values('numero')[0]

			p=ParientesCliente.objects.filter(cliente_id=cliente).values('nombre','edad','relacion__nombre')

			a[j]['parientes']=ValuesQuerySetToDict(p)

			a[j]['numero_hijos']=p.count()

		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")

class Citasagente(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def get(self, request):

		id =request.user.id

		agente = Agente.objects.get(user_id=id).id

		c =Citas.objects.filter(agente_id=agente).values('id','cliente__user','tipo_seguimiento__nombre','cliente__user__first_name','propuesta_cliente__ramo_compania_producto__ramo__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','propuesta_cliente__ramo_compania_producto__producto__nombre').order_by('-fecha_cita')

		#'cliente__user__first_name','agente__user__first_name','tipo_cita__nombre','',,,'tipo_seguimiento__nombre','observacion','prima_target','modalidad__nombre','prima_anual')
		
		fmt = '%d %b'

		
		for j in range(len(c)):

			if Citas.objects.get(id=c[j]['id']).fecha_cita:

				c[j]['fecha_cita'] = Citas.objects.get(id=c[j]['id']).fecha_cita.strftime(fmt)

		c= simplejson.dumps(ValuesQuerySetToDict(c))
		return HttpResponse(c, content_type="application/json")

class Termometro(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def get(self, request):

		id =request.user.id

		agente = Agente.objects.get(user_id=id).id
		
		ncitasreal = Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo').count()

		totalcitasesperado = (4*4+5)*5  #total de citas al anio

		citaesperadoafecha = (3*5)

		porcentajeesperado = citaesperadoafecha*100/totalcitasesperado



		porcentareal = float(ncitasreal*100/totalcitasesperado)


		if porcentajeesperado>porcentareal:
			estado='alerta'
		else:
			estado='exito'

		data={'estado':estado,'porcentaje':porcentareal,'porcentajeesperado':porcentajeesperado,'totalcitasesperado':totalcitasesperado}

		c= simplejson.dumps(data)
		return HttpResponse(c, content_type="application/json")


class Updatecita(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self, request):



		data = json.loads(request.body)


		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")


class Eliminarpropuesta(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,id):



		Citas.objects.filter(propuesta_cliente_id=id).delete()

		PropuestaCliente.objects.get(id=id).delete()


		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Eliminarcita(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,id):



		Citas.objects.get(id=id).delete()




		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")


class Userfono(JSONWebTokenAuthMixin, View):

	

	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)
		telefono=data['id']
		numero=data['numero']
		TelefonoUser(user_id=id,numero=numero).save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

	## Lista los telefonos
	def get(self,request):

		t=TelefonoUser.objects.filter('numero').values('numero')
		t= simplejson.dumps(ValuesQuerySetToDict(t))
    
		return HttpResponse(t, content_type="application/json")

    ## Elimina telefono
	def delete(self,request):

		TelefonoUser.objects.get(id=telefono).delete()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

	#Actualiza telefono
	def put(self,request):

		t=TelefonoUser.objects.get(id=telefono)
		t.numero= numero
		t.save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")


class CreaPariente(JSONWebTokenAuthMixin, View):

	#Crea nuevo cliente
	def post(self, request):

		data = json.loads(request.body)



		ParientesCliente(nombre=data['nombre'],fecha_nacimiento=data['fecha_nacimiento'],cliente_id=data['cliente'],relacion_id=data['relacion']).save()


		return HttpResponse(simplejson.dumps('cliente_id'), content_type="application/json")



class Creacliente(JSONWebTokenAuthMixin, View):

	#Crea nuevo cliente
	def post(self, request):

		id =request.user.id

	

		id_agente = Agente.objects.get(user_id=id).id

		id_equipo = AuthUser.objects.get(id=request.user.id).equipo.id

		data = json.loads(request.body)



		for i in data:

			print i

		fecha_inicio= None
		estado_civil= None
		numero_hijos= None
		first_name= None
		last_name= None
		email= None
		pais= None
		nacimiento= None
		dni= None
		direccion= None
		id_cliente= None
		telefono=None
		for i in data:

			print i

			if i=='fecha_inicio' : fecha_inicio = data['fecha_inicio']
			if i=='estado_civil' : estado_civil = data['estado_civil']
			if i=='numero_hijos' : numero_hijos = data['numero_hijos']
			if i=='first_name' : first_name = data['first_name']
			if i=='last_name' : last_name = data['last_name']
			if i=='email' : email = data['email']
			if i=='pais' : pais = data['pais']
			if i=='nacimiento' : nacimiento = data['nacimiento']
			if i=='dni' : dni = data['dni']
			if i=='direccion' : direccion = data['direccion']
			if i=='telefono' : telefono = data['telefono']

		print 'email',email

		if email== None:

			email = str(random.randint(1,21)*5)+'capital2017'

		if AuthUser.objects.filter(email=email).count()>0:

			return HttpResponse(simplejson.dumps('emailx'), content_type="application/json")


		au = User.objects.create_user(email,email,email)
		u_id = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

		u = AuthUser.objects.get(id=u_id)
		u.first_name = first_name
		u.last_name=last_name
		u.pais_id=pais

		# print nacimiento
		
		# nacimiento = datetime.datetime.strptime(nacimiento, '%Y-%m-%dT%H:%M:%S.%fZ')

		#2017-09-06T05:00:00.000Z
		# nacimiento = nacimiento.strftime('%Y-%m-%d')


		u.nacimiento=nacimiento
		u.dni=dni
		u.direccion=direccion
		u.save()

		## Telefono del usuario

		TelefonoUser(user_id=u_id,numero=telefono).save()

		c=Cliente(equipo_id=id_equipo,agente_id=id_agente,user_id=u_id,fecha_inicio=fecha_inicio,estado_civil=estado_civil,numero_hijos=numero_hijos).save()
		
		cliente_id = Cliente.objects.all().values('id').order_by('-id')[0]['id']
		
		Agentecliente(agente_id=id_agente,cliente_id=cliente_id).save()

		return HttpResponse(simplejson.dumps(cliente_id), content_type="application/json")

	#Actualiza cliente
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)

		print data

		telefono = None


		cliente = data['id']
		c=Cliente.objects.get(id=cliente)
		au =AuthUser.objects.get(id=c.user_id)

		for i in data:

			if i=='estado_civil' :c.estado_civil_id=data['estado_civil']
			if i=='numero_hijos' : c.numero_hijos=data['numero_hijos']
			if i=='first_name' : au.first_name=data['user__first_name']
			if i=='last_name' : au.last_name=data['user__last_name']
			if i=='email' : au.email=data['user__email']
			if i=='pais' : au.pais=data['user__pais']
			if i=='nacimiento' : au.nacimiento=data['user__nacimiento']
			if i=='telefono' : telefono=data['telefono']['numero']
			if i=='dni' : au.dni=data['user__dni']
			if i=='user__direccion' : au.direccion=data['user__direccion']

		c.save()
		au.save()


		if telefono:

			TelefonoUser(user_id=c.user.id,numero=telefono).save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

		
	
	#Informacion del cliente
	def get(self,request):

		data = json.loads(request.body)
		cliente=data['cliente']

		c =Cliente.objects.filter(id=cliente).values('fecha_inicio','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__nacimiento','user__dni','user__direccion')
		c= simplejson.dumps(ValuesQuerySetToDict(c))
		return HttpResponse(c, content_type="application/json")


class TodosClientes(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		id_agente = Agente.objects.get(user_id=request.user.id).id

		perfil = AuthUser.objects.get(id=request.user.id).nivel.nombre

		equipo = AuthUser.objects.get(id=request.user.id).equipo.nombre

		print 'perfil...'

		if perfil=='IFA':

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		
		if perfil=='Administrador':

			c =Cliente.objects.all().values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		
		if perfil=='Gerente':

			c =Cliente.objects.filter(equipo__nombre=equipo).values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		
		if perfil=='Gerente General':

			c =Cliente.objects.all().values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		

		#c =Cliente.objects.all().values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')
		c= simplejson.dumps(ValuesQuerySetToDict(c))
		return HttpResponse(c, content_type="application/json")

class Resumen(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self,request):

		id_agente =Agente.objects.get(user=request.user.id).id

		data = json.loads(request.body)

		s= data['semana']

		se = Semana.objects.filter(numero=s)

		nuevasvisitas=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

		seguimiento=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='Seguimiento').count()

		pos=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='POS').count()

		
		mes =data['mes']

		nvm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

		segm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='Seguimiento').count()

		posm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='POS').count()

		produccionmensual=[]

		montomensual = []

		for mes in range(12):

			produccionmensual.push(Citas.objects.filter(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre').count())
			
			m = Citas.objects.filter(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre')

			mm =0

			for x in m:
			
				mm=mm+Citas.objects.get(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre').prima_target
			
			montomensual.push(mm)
			
		data ={'produccionmensual':produccionmensual,'nvm':nvm,'segm':segm,'posm':posm,'nuevasvisitas':nuevasvisitas,'seguimiento':seguimiento,'pos':pos}

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")


class Produccionxcia(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		c =Agente.objects.get(user_id=request.user.id)

		c =Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__compania__nombre').annotate(citas=Count('propuesta_cliente__ramo_compania_producto__compania__nombre'))

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")


class Produccionxramo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		c =Agente.objects.get(user_id=request.user.id)

		c =Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(citas=Count('propuesta_cliente__ramo_compania_producto__ramo__nombre'))

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")




class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()	

class MiGestion(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		c =Agente.objects.get(user_id=request.user.id)

		avance = c.meta_personal*100/c.meta_requerida

		x = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre')

		totalcierres = x.count()

		totalcitas = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Nuevo').count()

		if totalcitas==0:

			efectividad = 0

		else:

			efectividad = totalcierres*100/totalcitas

		ytd=0

		for n in x:

			if n.prima_target:
				ytd =ytd+float(n.prima_target)


		from django.db.models import Count,Sum

		summary = (Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre')
		              .annotate(m=Month('fecha_cita'))
		              .values('m')
		              .annotate(total=Count('cliente'))
		              .annotate(produccion=Sum('prima_target'))
		              .order_by())

		for s in range(len(summary)):


			produccion_inforce = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre',inforce=1,fecha_cita__month=summary[s]['m']).annotate(produccion_inforce=Sum('prima_target')).values('produccion_inforce')

			pi = 0

			for p in range(len(produccion_inforce)):

				pi=pi+ produccion_inforce[p]['produccion_inforce']

			summary[s]['produccion_inforce']=pi

		#Produccion por compania

		cias = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__compania__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__compania'))
		
		ramos = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__ramo'))
		
		ramos = ValuesQuerySetToDict(ramos)

		cias = ValuesQuerySetToDict(cias)

		produccionmensual = ValuesQuerySetToDict(summary)
		#prodenero = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('fecha_cita__month').annotate(contador=Count('fecha_cita__month'))



		#print 'prodxmes',prodxmes


		ytdavance=ytd*100/c.meta_requerida

		if ytdavance >=100:
			ytdavance=100


		data={'ramos':ramos,'cias':cias,'produccionmensual':produccionmensual,'efectividad':efectividad,'ytdavance':ytdavance,'ytd':ytd,'meta_personal':c.meta_personal,'meta_requerida':c.meta_requerida,'avance':avance}
		data= simplejson.dumps(data)
		return HttpResponse(data, content_type="application/json")



class Metricas(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request,mes,dia,mes1,dia1):

		#Setiembre

		if len(mes)==1:
			mes='0'+mes
		if len(dia)==1:
			dia='0'+dia
		if len(dia1)==1:
			dia1='0'+dia1
		if len(mes1)==1:
			mes1='0'+mes1

		inicio= '2017-'+str(mes)+'-'+str(dia)

		fin = '2017-'+str(mes1)+'-'+str(dia1)

		inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d')

		fin = datetime.datetime.strptime(fin, '%Y-%m-%d')



		agente = Agente.objects.get(user_id=request.user.id).id



		c=Citas.objects.filter(agente_id=agente,fecha_cita__gte=inicio,fecha_cita__lte=fin).count()


		
		n =Citas.objects.filter(agente_id=agente,fecha_cita__gte=inicio,fecha_cita__lte=fin,tipo_seguimiento__nombre='Nuevo').count()

		p=0

		x={'c':c,'n':n,'p':0,'t':int(c)+int(n)+int(p)}

		c= simplejson.dumps(x)



		return HttpResponse(c, content_type="application/json")

class Creacita(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):

		data = json.loads(request.body)

		print data



		cliente=None
		tipo_cita=None
		propuesta_cliente=None
		tipo_seguimiento=None
		fecha_cita=None
		observacion=''
		fecha_solicitud=None
		prima_target=''
		modalidad=None
		prima_anual=''
		fecha_poliza=None
		seguimiento=None
		cierre=None
		poliza=None
		agente=Agente.objects.get(user=request.user.id).id



		for i in data:

			print 'i',i

			if i=='cliente': cliente=data['cliente']
			if i=='tipo_cita': tipo_cita=data['tipo_cita']
			if i=='tipo_seguimiento':tipo_seguimiento=data['tipo_seguimiento']
			if i=='propuesta': propuesta_cliente=data['propuesta']['id']

			for f in data['form']:

				if f=='observacion':observacion=data['form']['observacion']
				if f=='prima_target':prima_target=data['form']['prima_target']
				if f=='prima_anual':prima_anual=data['form']['prima_anual']
				if f=='fecha_cita': fecha_cita=data['form']['fecha_cita']
				if f=='fecha_solicitud': fecha_solicitud=data['form']['fecha_solicitud']
				if f=='modalidad': modalidad=data['form']['modalidad']['id']
				
		
			if i=='seguimiento': seguimiento=data['seguimiento']
			if i=='cierre': cierre=data['cierre']
			if i=='poliza': poliza=data['poliza']

		# if fecha_cita==None:
		fecha_creacion=datetime.datetime.now()


		print 'fecha_cita',fecha_cita


		#Cita... {u'seguimiento': 1, u'propuesta': {u'agente': None, u'ramo_compania_producto__compania__nombre': u'NWL', u'id': 8, u'ramo_compania_producto__producto__nombre': u'Index Select', u'cliente__user__first_name': u'Andy', u'ramo_compania_producto__ramo__nombre': u'Vida Int', u'cliente': 13}, u'cliente': u'13', u'form': {u'observacion': u'3232'}}

		if seguimiento==1: tipo_seguimiento=1
		if cierre==1:tipo_seguimiento=2
		if poliza==1:tipo_seguimiento=3

		tipo_cita= 2 ##Seguimiento




		Citas(fecha_creacion=fecha_creacion,agente_id=agente,tipo_seguimiento_id=tipo_seguimiento,cliente_id=cliente,tipo_cita_id=tipo_cita,propuesta_cliente_id=propuesta_cliente,observacion=observacion,fecha_cita=fecha_cita,fecha_solicitud=fecha_solicitud,prima_target=prima_target,modalidad_id=modalidad,prima_anual=prima_anual,fecha_poliza=fecha_poliza).save()


		c= simplejson.dumps('cliente')
		return HttpResponse(c, content_type="application/json")


class Creapos(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):

		data = json.loads(request.body)

		print data



		cliente=None
		tipo_cita=None
		propuesta_cliente=None
		tipo_seguimiento=None
		fecha_cita=None
		observacion=''
		fecha_solicitud=None
		prima_target=''
		modalidad=None
		prima_anual=''
		fecha_poliza=None
		seguimiento=None
		cierre=None
		poliza=None
		agente=Agente.objects.get(user=request.user.id).id

		
		for i in data:

			if i=='observacion': observacion=data['observacion']
			if i=='fecha_cita': fecha_cita=data['fecha_cita']
			if i=='pos':producto=data['pos']
			if i=='tipo_cita': tipo_cita=data['tipo_cita']
			if i=='cliente': cliente=data['cliente']

		tipo_cita= 3 # POS

		fecha_creacion=datetime.datetime.now()

		Citas(tipo_seguimiento_id=4,fecha_creacion=fecha_creacion,agente_id=agente,cliente_id=cliente,tipo_cita_id=tipo_cita,propuesta_cliente_id=producto,observacion=observacion,fecha_cita=fecha_cita).save()


		c= simplejson.dumps('cliente')
		return HttpResponse(c, content_type="application/json")


class Creapropuesta(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):

		data = json.loads(request.body)

		print data

		agente=Agente.objects.get(user=request.user.id).id


		cliente=None
		cia= None
		observacion=''
		compania= None
		producto=None
		rcp=None

		for i in data:

			if i=='cliente':cliente=data['cliente']
			if i=='observacion':observacion=data['observacion']
			if i=='cia':cia=data['cia']
			if i=='producto':producto=data['producto']
			if i=='ramo':ramo=data['ramo']['id']


		rcp=RamoCompaniaProducto.objects.get(compania_id=cia,ramo_id=ramo,producto_id=producto).id

		PropuestaCliente(cliente_id=cliente,fecha=datetime.datetime.now(),agente_id=agente,observacion=observacion,ramo_compania_producto_id=rcp).save()
		
		id_propuesta=PropuestaCliente.objects.all().values('id').order_by('-id')[0]['id']

		Citas(tipo_seguimiento_id=5,fecha_creacion=datetime.datetime.now(),agente_id=agente,cliente_id=cliente,tipo_cita_id=1,propuesta_cliente_id=id_propuesta,observacion=observacion,fecha_cita=datetime.datetime.now()).save()


		c= simplejson.dumps(cliente)
		return HttpResponse(c, content_type="application/json")


	#Actualizapropuesta
	def put(self, request):

		data = json.loads(request.body)
		propuesta = data['propuesta']

		p=PropuestaCliente.objects.get(id=propuesta)

		for i in data:
			if i=='cliente':p.cliente=data['cliente']
			if i=='agente':p.agente=data['agente']
			if i=='observacion':p.observacion=data['observacion']
			if i=='fecha':p.fecha=data['fecha']
			if i=='detalle':p.detalle=data['detalle']
			if i=='ramo_compania_producto':p.ramo_compania_producto=data['ramo_compania_producto']

		p.save()
		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Listaramos(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Ramo.objects.all().values('id','nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")

class ListaModalidad(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Modalidad.objects.all().values('id','nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Losarchivos(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Archivo.objects.all().values('id','nombre','ruta')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class IconosLista(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Iconos.objects.all().values('id','nombre','icono').order_by('id')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Semanasall(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Semanas.objects.all().values('id','numero').order_by('-id')

		fmt = '%d %b'

		for j in range(len(r)):

			r[j]['fecha_inicio'] = Semanas.objects.get(id=r[j]['id']).fecha_inicio.strftime(fmt)
			r[j]['fecha_fin'] = Semanas.objects.get(id=r[j]['id']).fecha_fin.strftime(fmt)
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")



class Calculomes(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

	
		agente=Agente.objects.get(user=request.user.id).id

		# Por mes

		ncitasmes = (Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo')
		              .annotate(m=Month('fecha_cita'))
		              .values('m')
		              .annotate(total=Count('cliente'))
		              .annotate(produccion=Sum('prima_target'))
		              .order_by())

		ncitasmes= simplejson.dumps(ValuesQuerySetToDict(ncitasmes))

		nseguimientomes = (Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Seguimiento de Prospectos')
		              .annotate(m=Month('fecha_cita'))
		              .values('m')
		              .annotate(total=Count('cliente'))
		              .annotate(produccion=Sum('prima_target'))
		              .order_by())

		nseguimientomes= simplejson.dumps(ValuesQuerySetToDict(nseguimientomes))

		nposmes = (Citas.objects.filter(agente_id=agente,tipo_cita__nombre='POS')
		              .annotate(m=Month('fecha_cita'))
		              .values('m')
		              .annotate(total=Count('cliente'))
		              .annotate(produccion=Sum('prima_target'))
		              .order_by())

		nposmes= simplejson.dumps(ValuesQuerySetToDict(nposmes))


		r={'ncitasmes':ncitasmes,'nseguimientomes':nseguimientomes,'nposmes':nposmes}

		r= simplejson.dumps(r)
		return HttpResponse(r, content_type="application/json")


class Calculo(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,semana):

		s=Semanas.objects.get(numero=semana)


		agente=Agente.objects.get(user=request.user.id).id

		#Intervalos de fechas

		nuevascitas = Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()

		nseguimiento = Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Seguimiento de Prospectos',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()

		npos = Citas.objects.filter(agente_id=agente,tipo_cita__nombre='POS',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()




		r={'ncitas':nuevascitas,'nseguimiento':nseguimiento,'npos':npos}

		r= simplejson.dumps(r)
		return HttpResponse(r, content_type="application/json")


class Detallepropuesta(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,id):

		r=PropuestaCliente.objects.filter(id=id).values('observacion','id','agente','cliente','ramo_compania_producto__ramo__nombre','ramo_compania_producto__compania__nombre','ramo_compania_producto__producto__nombre','cliente__user__first_name')
		
		fmt = '%Y-%m-%d'

		for j in range(len(r)):

			if PropuestaCliente.objects.get(id=r[j]['id']).fecha:

				r[j]['fecha'] = PropuestaCliente.objects.get(id=r[j]['id']).fecha.strftime(fmt)

		r= simplejson.dumps(ValuesQuerySetToDict(r))

		return HttpResponse(r, content_type="application/json")





class Listacia(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,ramo):

		r=RamoCompaniaProducto.objects.filter(ramo_id=ramo).values('compania','compania__nombre').annotate(c=Max('compania'))
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Listaproducto(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,ramo,cia):

		r=RamoCompaniaProducto.objects.filter(ramo_id=ramo,compania_id=cia).values('id','producto','producto__nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Listapropuestas(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,cliente):

		r=PropuestaCliente.objects.filter(cliente_id=cliente).values('id','cliente','agente','ramo_compania_producto__ramo__nombre','ramo_compania_producto__compania__nombre','ramo_compania_producto__producto__nombre')
		
		for j in range(len(r)):

			if Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre'):

				r[j]['cierre']=1

			else:

				r[j]['cierre']=0


		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")
