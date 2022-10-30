from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from main.forms import *
from main.models import *


def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'main/show_products.html', context)


def add_form(request):
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            random_content = form.cleaned_data
            context = {
                'random_content': random_content
            }

            return render(request, 'main/display_random.html', context)
    else:
        form = RandomForm()

        context = {
            'form': form
        }

        return render(request, 'main/add_prod_form.html', context)


def add_product_modelform(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_products')

    else:
        form = ProductModelForm()

    context = {
        'form': form
    }

    return render(request, 'main/add_product_modelform.html', context)


def add_product_input(request):
    categories = Category.objects.all()
    shops = Shop.objects.all()

    if request.method == 'POST':
        form_values = {}
        form_values['title'] = request.POST.get('title')
        form_values['description'] = request.POST.get('description')
        form_values['price'] = request.POST.get('price')
        form_values['category_id'] = request.POST.get('category')

        new_product = Product.objects.create(**form_values)
        new_product.save()

        chosen_shops_ids = request.POST.getlist('shop')
        for shop_id in chosen_shops_ids:
            chosen_shop = Shop.objects.get(pk=shop_id)
            chosen_shop.product_set.add(new_product)

        return redirect('main:show_products')

    context = {
        'categories': categories,
        'shops': shops
    }

    return render(request, 'main/add_product_input.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product': product
    }

    return render(request, 'main/product_detail.html', context)


def product_update(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    shops = Shop.objects.all()

    context = {
        'product': product,
        'categories': categories,
        'shops': shops
    }

    if request.method == 'POST':
        new_values = {'id': id}
        new_values['title'] = request.POST.get('title')
        new_values['description'] = request.POST.get('description')
        new_values['price'] = request.POST.get('price')
        new_values['category_id'] = request.POST.get('category')

        upd_product = Product(**new_values)
        upd_product.save()

        chosen_shops_ids = request.POST.getlist('shop')
        print(chosen_shops_ids)
        for shop_id in chosen_shops_ids:
            try:
                chosen_shop = Shop.objects.get(pk=shop_id)
                chosen_shop.product_set.set([upd_product])
            except ObjectDoesNotExist:
                return render(request, 'main/product_update.html', context)

        return redirect('main:product_detail', id=id)

    return render(request, 'main/product_update.html', context)


def product_update_modelform(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product_form = ProductModelForm(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('main:product_detail', id=id)
        else:
            context = {
                'product_form': product_form
            }
            return render(request, 'main/product_update_modelform.html', context)
    else:
        product_form = ProductModelForm(instance=product)
        context = {
            'product_form': product_form
        }
        return render(request, 'main/product_update_modelform.html', context)

def product_delete(request, id):
    product = Product.objects.get(id=id)
    connected_shops = product.shops.all()

    for connected_shop in connected_shops:
        connected_shop.product_set.remove(product)

    product.delete()

    return redirect('main:show_products')
