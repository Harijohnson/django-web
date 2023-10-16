from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your views here.

def store(request):
    products=Product.objects.all()
    context={'products': products}
    #add some git chnages
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, compleate=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context={'items': items,'order':order}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, compleate=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context={'items': items,'order':order}
    return render(request,'store/checkout.html',context)


def updateItem(request):
    # data=json.loads(request.data)
    # productId=data['productId']
    # action=data['action']

    # print(productId,action)
    return JsonResponse('item was added successfully',safe=False)






























