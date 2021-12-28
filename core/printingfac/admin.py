from django.contrib import admin
from .models import customerservice, supplier,Customer,material,factory
# Register your models here.
admin.site.register(supplier)
admin.site.register(Customer)
admin.site.register(material)
admin.site.register(factory)
admin.site.register(customerservice)
