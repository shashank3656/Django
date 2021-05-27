from django.shortcuts import render,redirect
from .models import publishedblog,draftblog
from userprofile.models import User_profileing
from django.http import HttpResponse

import base64
from PIL import Image
from io import BytesIO
import random


# Create your views here.
def home(request):
	#print(1)
	u=request.user.username
	usr=User_profileing.objects.get(username=request.user)
	#print(usr)
	img=usr.image64
	#print(usr.id)
	pb=publishedblog.objects.filter(byuser=usr.id)
	#print(pb)
	return render(request,'dashboard.html',{'name':u,'image':img,'lblog':pb.last()})


def addblog(request):
	uno=request.user.username
	uid=request.user.id
	url=''
	if request.method=='POST':
		ndr=request.POST['submit']
		ntitle=request.POST['title']
		nsummary=request.POST['summary']
		ncontent=request.POST['content']
		
		nbyuser=request.POST['user']

		nimage1=request.FILES['blogimage1']
		nimage2=request.FILES['blogimage2']
		nimage3=request.FILES['blogimage3']

		ntag=request.POST['tag']
		#imgfile=request.FILES.getlist('image')
		#print(imgfile)
		#print(ndraft)

		usr=User_profileing.objects.get(id=int(nbyuser))
		if ndr=='Draft':
			n=draftblog(dtitle=ntitle,dsummary=nsummary,dcontent=ncontent,dimage1=nimage1,dimage2=nimage2,dimage3=nimage3,dbyuser=usr,dtags=ntag)
			n.save()
		elif ndr=='Publish':
			m=publishedblog(title=ntitle,summary=nsummary,content=ncontent,image1=nimage1,image2=nimage2,image3=nimage3,byuser=usr,tags=ntag)
			m.save()

		return HttpResponse('<script>alert("Blog Saved");window.location="%s"</script>'%url)

	return render(request,'addblog.html',{'name':uno,'id':uid})

	

def draft(request):
	u=User_profileing.objects.get(username=request.user)
	n=draftblog.objects.filter(dbyuser=u)
	#print(n)
	return render(request,'draft.html',{'name':u.username,'db':n})

def published(request):
	u=User_profileing.objects.get(username=request.user)
	p=publishedblog.objects.filter(byuser=u)
	return render(request,'published.html',{'name':u.username,'pb':p})



def showblog(request,id):
	u=User_profileing.objects.get(username=request.user)
	p=publishedblog.objects.get(id=id)
	return render(request,'showblog.html',{'blog':p,'name':u.username})

def drafttopub(request,id):
	url=""
	try:
		d=draftblog.objects.get(id=id)
		#print(d.dimage2,d.dimage3)
		#u=User_profileing.objects.get(username=d.dbyuser)

		p=publishedblog(title=d.dtitle,summary=d.dsummary,content=d.dcontent,image1=d.dimage1,image2=d.dimage2,image3=d.dimage3,byuser=d.dbyuser)
		#print(p)
		p.save()
		#print('here')
		d2=draftblog.objects.filter(id=id)
		d2.delete()

		return HttpResponse('<script>alert("Blog Published");window.location="%s"</script>'%url)

	except:
		return redirect('/blog/draft')
		
	return redirect('/blog/draft')

def search(request):
	u=User_profileing.objects.get(username=request.user)
	
	st=request.POST['searchtext']
	print(st)

	return render(request,'search.html',{'name':u.username})

	