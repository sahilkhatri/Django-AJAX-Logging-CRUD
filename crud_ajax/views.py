from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from .models import CrudUser

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

# global list which will hold the details for each log/action/request performed
logdata=[]


# view for the main page i.e. crud.html
class CrudView(ListView):
	model = CrudUser
	template_name = 'crud_ajax/crud.html'
	context_object_name = 'users'

# view for the log page i.e. log.html
class LogView(TemplateView):
	template_name = 'crud_ajax/log.html'
	context_object_name = 'logdata'


# display function is used for the functionality to showcase all the users in a paginated in main page
def display(request):
	context = {}
	user_list = CrudUser.objects.all()
	paginator = Paginator(user_list, 5)						# paginated list with upto 5 entries in each page
	first_page = paginator.page(1).object_list				# first page data
	page_range = paginator.page_range						# range of pages
	context = {
	'paginator':paginator,
	'first_page':first_page,
	'page_range':page_range,
	}
	if request.method == 'POST':
		#getting page number
		page_no = request.POST.get('page_no', 1) 
		results = list(paginator.page(page_no).object_list.values('id','username','firstname','lastname','email'))
		print(results)
		return JsonResponse({"results":results})
	elif request.method == 'GET':
		#getting page number
		page_no = request.POST.get('page_no', 1) 
		results = list(paginator.page(page_no).object_list.values('id','username','firstname','lastname','email'))
		return JsonResponse({"results":results})
	else:
		#page_no = request.POST.get('page_no', 1) 
		results = list(paginator.page(1).object_list.values('id','username','firstname','lastname','email'))
		return JsonResponse({"results":results})




from .models import CrudUser
from django.views.generic import View
from django.http import JsonResponse
from datetime import datetime

# CreateCrudUser class is used to get the details of the Newly added user from the ajax function 
# and the details are inserted into the CrudUser model. 
# And it returns the dictionary of the details that are inserted.
# This retured dictionary is used to show the response of the ADD user functionality.
class CreateCrudUser(View):
	def  get(self, request):
		username1 = request.GET.get('username', None)
		firstname1 = request.GET.get('firstname', None)
		lastname1 = request.GET.get('lastname', None)
		email1 = request.GET.get('email', None)
		
		obj = CrudUser.objects.create(
			username = username1,
			firstname = firstname1,
			lastname = lastname1,
			email = email1
		)

		user = {'id':obj.id,'username':obj.username,'firstname':obj.firstname,'lastname':obj.lastname,'email':obj.email}

		data = {
			'user': user
		}
		global logdata
		logdata.append({'action':'POST/Create','id':obj.id, 'time':datetime.now()})

		return JsonResponse(data)


# UpdateCrudUser class is used to get the details of the Newly updated user from the ajax function 
# and the details are updated into the CrudUser model. 
# And it returns the dictionary of the details that are updated.
# This retured dictionary is used to show the response of the UPDATE user functionality.
class UpdateCrudUser(View):
	def  get(self, request):
		id1 = request.GET.get('id', None)
		username1 = request.GET.get('username', None)
		firstname1 = request.GET.get('firstname', None)
		lastname1 = request.GET.get('lastname', None)
		email1 = request.GET.get('email', None)

		obj = CrudUser.objects.get(id=id1)
		obj.username = username1
		obj.firstname = firstname1
		obj.lastname = lastname1
		obj.email = email1
		obj.save()

		user = {'id':obj.id,'username':obj.username,'firstname':obj.firstname,'lastname':obj.lastname,'email':obj.email}

		data = {
			'user': user
		}
		global logdata
		logdata.append({'action':'PUT/Update','id':obj.id, 'time':datetime.now()})
		return JsonResponse(data)

# DeleteCrudUser class is used to get the details of the user to be DELETED from the ajax function 
# and the details are deleted from the CrudUser model. And it returns the dictionary of the details that are removed.
# This retured dictionary is used to show the response of the DELETE User functionality.
class DeleteCrudUser(View):
	def get(self, request):
		id1 = request.GET.get('id', None)
		obj = CrudUser.objects.get(id=id1)
		CrudUser.objects.get(id=id1).delete()
		user = {'id':obj.id,'username':obj.username,'firstname':obj.firstname,'lastname':obj.lastname,'email':obj.email}
		data = {
			'deleted':True,
			'user':user,
		}
		global logdata
		logdata.append({'action':"Delete",'id':obj.id, 'time':datetime.now()})
		return JsonResponse(data)

# ShowCrudUser class is used to get the details of the desired USER from the ajax function. 
# The details are fetched from the CrudUser model based on the userid. 
# And it returns the dictionary of the details that are requested.
# This retured dictionary is used to show the response of the READ user functionality.
class ShowCrudUser(View):
	def get(self, request):
		id1 = request.GET.get('id', None)
		obj = CrudUser.objects.get(id=id1)
		foo = {'id':obj.id,'username':obj.username,'firstname':obj.firstname,'lastname':obj.lastname,'email':obj.email}
		data = {
			'user': foo
		}
		global logdata
		logdata.append({'action':'GET/Read','id':obj.id, 'time':datetime.now()})
		return JsonResponse(data)

# displaylogs function is used to show the paginated view of all the users requests that made on the main page.
# This will enable to show upto 10 log entries per page in the log.html
def displaylogs(request):
	context = {}
	global logdata
	paginator = Paginator(logdata, 10)
	first_page = paginator.page(1).object_list
	page_range = paginator.page_range
	context = {
	'paginator':paginator,
	'first_page':first_page,
	'page_range':page_range,
	}
	print(page_range)
	print(request.POST.get('page_no'))
	if request.method == 'POST':
		page_no = request.POST.get('page_no', 1) 
		results = list(paginator.page(page_no).object_list)
		return JsonResponse({"results":results})
