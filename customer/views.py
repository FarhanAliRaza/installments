from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Customer, Month, Plan, Item
from . forms import ItemForm
from customer.month import  Mon
from django.utils import timezone
from django.contrib import messages

import datetime
def home(request):
    items = Item.objects.all().order_by('-total_pending')
    total_rcvd = 0
    total_pend = 0 
    for i in items:
        total_rcvd = total_rcvd + i.total_recieved
        total_pend = total_pend + i.total_pending
    

    return render(request, 'home.html', {'items' : items, 'tr' : total_rcvd, 'tp' : total_pend, 'num' : len(items)})

def create_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        cnic = request.POST.get('cnic')

        ref = request.POST.get('ref')
        adress = request.POST.get('adress')
        Customer.objects.create(name =username, phone = phone, ref_name = ref , adress = adress, cnic = cnic)
        return redirect("/")


    return render(request, 'createuser.html', {})
months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']

def detail_item(request, id):
    item = Item.objects.get(id = id)
    mons = item.plan.months.all()
    return render(request, 'items.html', {'months' : mons, 'cus' : item.customer, 'item' : item})

def update_month(request, item_id, id):
    item = Item.objects.get(id = item_id)
    mon = Month.objects.get(id = id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        amount = int(amount)
        print(amount)
        mon.recieved = amount
        x = mon.total - amount
        if x < 0:
            messages.add_message(request, messages.INFO, 'Value larger than installment value not allowed')

            return render(request, 'updatemon.html', {})


        mon.pending = x


        mon.save()
        item.total_recieved = item.total_recieved + amount
        item.total_pending = item.total_pending - amount
        item.save()
        return redirect(f"/item/{item_id}/")


        


    return render(request, 'updatemon.html', {'item' : item, 'mon' : mon})

def customer_delete(request, id):
    
    i = Item.objects.get(id=id)
    i.delete()
    return redirect("/")



def create_item(request):
    form = ItemForm()
    if request.method == 'POST':
        print(request.POST)
        f = ItemForm(request.POST)
        if f.is_valid():

            item = Item.objects.create(
                item_name = f.cleaned_data['item_name'],
                 total_amount  = f.cleaned_data['total_amount'],
                 advance_taken = f.cleaned_data['advance_taken'],
                 total_kist_months = f.cleaned_data['total_kist_months'],
                 total_recieved = f.cleaned_data['advance_taken'],
                 total_pending = f.cleaned_data['total_amount'] - f.cleaned_data['advance_taken'],
                 customer = f.cleaned_data['customer'],
                 net_rate = f.cleaned_data['net_rate'],
                 qty = f.cleaned_data['qty'],
                 imei = f.cleaned_data['imei'],
                 amount_in_words = f.cleaned_data['amount_in_words'],
                 timestamp = timezone.now()

                 
                 )
            ta = f.cleaned_data['total_amount']
            advt = f.cleaned_data['advance_taken']
            tk = f.cleaned_data['total_kist_months']

            tl = ta - advt
            per_mon = tl // int(tk)
            print(per_mon)
            item.kist = per_mon
            t = datetime.date.today()
            mon = Mon(t.month)
            p = Plan.objects.create()
            for i in range(int(tk)):
                m = Month.objects.create(name = months[mon.get_next_month()], year = t.year, total = per_mon, pending = 0, recieved = 0)
                p.months.add(m)
            p.save()
            item.plan = p
            item.save()
            return redirect("/")



    return render(request, 'createitem.html', {'form' : form})

def invoice(request, id):
    item = Item.objects.get(id = id)
    return render(request, 'invoice.html', {'item' : item})

def invoices(request):
    items = Item.objects.all()
    return render(request, 'invoices.html', {'items' : items})



def pages(request):
    context = {}
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
