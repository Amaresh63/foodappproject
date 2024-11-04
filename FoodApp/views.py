# from django.http import HttpResponse
# from django.http import HttpResponse
from django.shortcuts import render
from FoodApp.models import Item
from FoodApp.forms import ItemForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'FoodApp/index.html',context)
def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    } 
    return render(request,'FoodApp/details.html',context)

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:index') 
    return render(request,'FoodApp/item_form.html',{'forms':form})
def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('FoodApp:index')
    return render(request,'FoodApp/item_form.html',{'forms':form})
def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('FoodApp:index')
    return render(request,'FoodApp/delete_msg.html',{'item':item})
