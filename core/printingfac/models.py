from django.db import models

# Create your models here.
class supplier(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    
class material(models.Model):
    name=models.CharField(max_length=30)
    supplier_associated=models.ForeignKey(supplier,related_name='sup',on_delete=models.CASCADE) 
    
class Customer(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class factory(models.Model):
    name=models.CharField(max_length=20)
    supplier_to_associate_request=models.ForeignKey(supplier,related_name='sta',on_delete=models.CASCADE)
    material_id=models.ForeignKey(material,related_name='materials',on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,related_name='customers',on_delete=models.CASCADE)
    date_of_order=models.DateTimeField()
    quantity=models.IntegerField()
    brand=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    rate=models.IntegerField()
    amount=models.IntegerField()
    tax=models.CharField(max_length=7)
    tax_amount=models.CharField(max_length=10)
    status=models.BooleanField()
class customerservice(models.Model):
    name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=30)
    ph_no=models.IntegerField()
    issues=models.CharField(max_length=30)


   

    
    
