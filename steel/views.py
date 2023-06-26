from django.shortcuts import render,redirect
from .models import *
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.contrib import messages
from django.http.response import JsonResponse
# Create your views here.

def home(request):
    cats=Category.objects.all()
    context={'cats':cats}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html',{})

def category(request,cat):
    if Category.objects.filter(name=cat):
        c=Category.objects.get(name=cat)
        print(cat)
        products=Product.objects.filter(category=c)
        context={'cat':cat,'product':products}
        return render(request,'category.html',context)
    else:
        return redirect('home')
    

def contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
    else:
        email=request.POST['email']
        name=request.POST['c_name']
        phone_no=request.POST['p_no']
        query=request.POST['query']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        firmname=request.POST['firmname']
    

        send_mail(
            'Customer Contact',
            f'''
            Name : {name}
            Phone number : {phone_no}
            Email Id : {email}
            Firm : {firmname}
            City : {city}
            State : {state}
            Pincode : {pincode}
            Customer query: {query}
            ''',
            'steeltechengineers4@gmail.com',       #   gmail
            ['steeltechengineers4@gmail.com'],
            fail_silently=False

        )
        send_mail(
            'Steeltech Enginners',
            f'Thank you {name} for contacting with steel tech engineers...we will contact you shortly',
            'steeltechengineers4@gmail.com',
            [email],
            fail_silently=False

        )

        messages.success(request,'Your Query has been recived , We will contact you shortly')
        return redirect('home')
    
def productlist(request):
    p=Product.objects.all().values_list('name',flat=True)
    products=list(p)
    return JsonResponse(products,safe=False)

def search(request):
    if request.method=='POST':
        searchedterm=request.POST['productsearch']
        print(searchedterm)
        if searchedterm=='':
            return redirect('home')
        else:
            product=Product.objects.filter(name__contains=searchedterm).first()
            if product:
                return redirect('product',product.id)
            else:
                messages.error(request,'No such product found')
                return redirect('home')
    
    return redirect('home')

def product(request,id):
    if request.method=='GET':
        product=Product.objects.filter(id=id).first()
        if product:
            return render(request,'product.html',{'product':product})
        else:
            messages.error(request,'OOPS ! No such product available')
            return redirect('home')
    return redirect('home')


            

    
    



