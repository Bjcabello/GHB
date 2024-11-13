
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    image = models.ImageField(upload_to='productos/', verbose_name='Imagen')
    available = models.BooleanField(default=True, verbose_name='Disponible')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    amount = models.PositiveIntegerField(verbose_name='Cantidad')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Órdenes'

    def __str__(self):
        return f"Orden {self.id} - {self.product.name}"


