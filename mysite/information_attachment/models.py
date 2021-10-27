from django.db import models
from django.urls import reverse
import uuid

class Product(models.Model):
    number = models.CharField('Number', max_length=200, help_text='Enter product number')

    link = "Edit"

    STATUS = (
        ('available', 'Available'),
        ('ordered', 'Ordered'),
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS,
        blank=True,
        default='available',
        help_text='Status',
    )

    def __str__(self):
        return f'{self.number} is {self.status}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class OrderProduct(models.Model):
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, related_name='products')

    link = "Edit"

    def __str__(self):
        return f"{self.order.number}: {self.product.number}"

    def get_absolute_url(self):
        return reverse('order', args=[str(self.id)])

    class Meta:
        verbose_name = 'Order product'
        verbose_name_plural = 'Order products'

class ImageOrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique product picture ID')
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_pictures', blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.order_product.product.number}"

    @classmethod
    def create(cls, order_product_id):
        image_order_product = cls(order_product=order_product_id)
        return image_order_product

class Order(models.Model):
    number = models.CharField('Number', max_length=200, help_text='Enter order number')
    ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    order_info = models.FileField(upload_to='order files', blank=True, null=True)

    link = "Edit"

    STATUS = (
        ('order placed', 'Order placed'),
        ('in progress', 'In progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS,
        blank=True,
        default='order placed',
        help_text='Status',
    )

    def __str__(self):
        return f"{self.number} {self.date_created}"

    def display_products(self):
        return ', '.join(product.product.number for product in self.products.all()[:3])

    def order_products(self):
        return ', '.join(product.product.number for product in self.products.all()[:3])

    def get_absolute_url(self):
        return reverse('order', args=[str(self.id)])

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class ImageOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique order picture ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='order_pictures')

    def __str__(self):
        return f"{self.id} {self.order} {self.image}"
