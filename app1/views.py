from django.shortcuts import render
from app1.models import *
from django.http import *
# Create your views here.
def display_topics(request):
    if request.method=='POST':
        topic_name=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=topic_name)[0]
        to.save()
        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render(request,'display_topic.html',d)
    

    return render(request,'topic.html')

def display_webpage(request):
   TO=Topic.objects.all()
   d2={'webpages':TO}
   if request.method=='POST':
       tn=request.POST['tn']
       na=request.POST['na']
       ur=request.POST['ur']
       em=request.POST['em']

       WO=Topic.objects.get(topic_name=tn)
       QLWO=Webpage.objects.get_or_create(topic_name=WO,name=na,url=ur,email=em)[0]
       QLWO.save()
       QLWO1=Webpage.objects.all()
       d3={'web':QLWO1}
       return render(request,'display_webpage.html',d3)


  
       



   return render(request,'insert_webpage.html',d2)

def select_multiple_webpage(request):
    TO=Topic.objects.all()
    d={'webpages':TO}
    if request.method=='POST':
        topic_list=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for tn in topic_list:
            QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
        d1={'web':QLWO}
        return render(request,'display_webpage.html',d1)
    


    return render(request,'select_multiple.html',d)

def checkbox(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    '''if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for tn in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
        d1={'web':QLWO}
        return render(request,'display_webpage.html',d1)'''


    return render(request,'checkbox.html',d)



def insert_records(request):
    WO=Webpage.objects.all()
    d={'records':WO}
    if request.method=='POST':
        pk=request.POST['pk']
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']

        a=Webpage.objects.get(pk=pk)
        QLAR=AccessRecord.objects.get_or_create(pk=a,name=na,date=da,author=au)[0]
        QLAR.save()
        QLAR1=AccessRecord.objects.all()
        d1={'records':QLAR1}
        return render(request,'display_records.html',d1)



    return render(request,'insert_records.html',d)

def display_records(request):
    QLAR=AccessRecord.objects.all()
    d={'records':QLAR}
    return render(request,'display_records.html',d)
