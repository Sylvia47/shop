from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from items.form import OrderForm




def category01(request):
    '''
    Render the category01 page
    '''
    return render(request, 'items/category01.html')


def category02(request):
    '''
    Render the category02 page
    '''
    return render(request, 'items/category02.html')

def category03(request):
    '''
    Render the category03 page
    '''
    return render(request, 'items/category03.html')

def category04(request):
    '''
    Render the category02 page
    '''
    return render(request, 'items/category04.html')

def category05(request):
    '''
    Render the category05 page
    '''
    return render(request, 'items/category05.html')

def category06(request):
    '''
    Render the category06 page
    '''
    return render(request, 'items/category06.html')

@login_required
def orderCreate(request):
    template = 'items/orderCreate.html'
    if request.method == 'GET':
        return render(request, template, {'orderForm':OrderForm()})
    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':OrderForm})

    orderForm.save()
    return category01(request)
# Create your views here.
