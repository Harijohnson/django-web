from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import  cookieCart,cartData,guestOrder

# Create your views here.

def store(request):
    data=cartData(request)
    cartItems= data['cartItems']

    products=Product.objects.all()
    context={'products': products, 'cartItems': cartItems}
    return render(request,'store/store.html',context)
def cart(request):
    data=cartData(request)
    cartItems= data['cartItems']
    order =data['order']
    items = data['items']

    context={'items': items,'order':order,'cartItems': cartItems}
    return render(request,'store/cart.html',context)

def checkout(request):
    data=cartData(request)
    cartItems= data['cartItems']
    order =data['order']
    items = data['items']

    context={'items': items,'order':order,'cartItems': cartItems}
    return render(request,'store/checkout.html',context)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    # print('productId:'+str(productId))
    # print('action:'+str(action))
    # print(productId,action)



    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer, compleate=False)
    
    orderItem,created=OrderItem.objects.get_or_create(order=order, product=product)
    #print(orderItem)
    
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif  action =='remove':
        orderItem.quantity=(orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('item was added successfully',safe=False)


def processOrder(request):
    transation_id = datetime.datetime.now().timestamp()
    print('transatction_id is here :',transation_id)
    data = json.loads(request.body)
    print("here is transaction detail",transation_id, data)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer, compleate=False)
    else:
        customer,order = guestOrder(request,data)

    total= float(data['form']['total'])
    order.transation_id = transation_id

    
    if total == order.get_cart_total:
        order.compleate = True
    order.save()
    if order.shipping == True:
            ShippingAddress.objects.create(
                customer= customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                country=data['shipping']['country'],
            )
    return JsonResponse('payment completed',safe=False)



























