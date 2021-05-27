from django.shortcuts import render,redirect
from blog.models import publishedblog
import random


def home(request):
	try:
		pb=publishedblog.objects.all().last()
		number_of_records = publishedblog.objects.count()
		random_index = int(random.random()*number_of_records)+1
		r=int(random_index)-1
		ra=int(random_index)-2
		nb1= publishedblog.objects.get(id = random_index)
		#print(nb1)
		nb2= publishedblog.objects.get(id = r)
		#print(nb2)
		nb3= publishedblog.objects.get(id = ra)
		#print(nb3)
	except:
		return render(request,'error.html')
		
	return render(request,'index.html',{'lblog':pb,'nb1':nb1,'nb2':nb2,'nb3':nb3})