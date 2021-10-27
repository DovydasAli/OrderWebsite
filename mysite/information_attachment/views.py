from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, OrderProduct, Order, ImageOrderProduct, ImageOrder

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q

from django.shortcuts import get_object_or_404

import time
import cv2
import uuid

def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_products = Product.objects.all().count()
    num_orders = Order.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_products_available = Product.objects.filter(status__exact='available').count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_products': num_products,
        'num_orders': num_orders,
        'num_products_available': num_products_available,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

def orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context=context)

def order(request, order_id):
    single_order = get_object_or_404(Order, pk=order_id)
    order_product_picture = ImageOrderProduct.objects.filter(order_product__order__id=order_id)
    return render(request, 'order.html', {'order': single_order, 'order_product_picture': order_product_picture})

def add_pictures(request, product_id):
    # order_product_id = ImageOrderProduct.create(product_id)
    for x in range(3):
        camera_port = x
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        cv2.imwrite(f'{uuid.uuid4()}.png', image)
        del (camera)  # so that others can use the camera as soon as possible
        product_image = ImageOrderProduct(order_product=product_id, image=image, id=uuid.uuid4())
        product_image.save()
    return HttpResponse("good job")

def take_pictures(request):
    for x in range(3):
        camera_port = x
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        cv2.imwrite(f'{uuid.uuid4()}.png', image)
        del (camera)  # so that others can use the camera as soon as possible
    return HttpResponse("good job")

class OrderProductCreateView(CreateView):
    model = OrderProduct
    fields = ['product', 'order']
    template_name = 'order_product_form.html'
    success_url = "/information_attachment/orders/"

class OrderCreateView(CreateView):
    model = Order
    fields = ['number', 'order_info']
    template_name = 'order_form.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['number', 'order_info']
    template_name = 'order_form.html'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/information_attachment/orders/"
    template_name = 'order_delete_form.html'

class ImageOrderProductCreateView(CreateView):
    model = ImageOrderProduct
    fields = ['order_product', 'image']
    template_name = 'image_order_product_form.html'
    success_url = "/information_attachment/orders/"

class SearchResultsView(ListView):
    model = Order
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Order.objects.filter(
            Q(number__icontains=query)
        )
        return object_list