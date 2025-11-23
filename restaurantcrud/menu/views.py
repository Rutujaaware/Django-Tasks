from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuItemForm

# READ
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})

# CREATE
def menu_create(request):
    form = MenuItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'menu/menu_form.html', {'form': form})

# UPDATE
def menu_update(request, id):
    item = get_object_or_404(MenuItem, id=id)
    form = MenuItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'menu/menu_form.html', {'form': form})

# DELETE
def menu_delete(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm_delete.html', {'item': item})
