from django.shortcuts import render
from user_core.models import Site
# Create your views here.


def about(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'about.html',context)
                
def assets(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    
    return render(request,'assets.html',context)
                
def contact(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    
    return render(request,'contact.html',context)
                
def faq(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'faq.html',context)
                
def index(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    
    return render(request,'index.html',context)
                
def payment_policy(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'payment-policy.html',context)
                
def policy(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'policy.html',context)
                
def privacy_policy(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'privacy-policy.html',context)
                
def terms_and_conditions(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'terms-and-conditions.html',context)
                #views created
