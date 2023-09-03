from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    prize = models.PositiveIntegerField()
    productimage1 = CloudinaryField('images')
    productimage2 = CloudinaryField('images')
    productimage3 = CloudinaryField('images')
    productimage4 = CloudinaryField('images')
    def __str__(self):
	    return str(self.name)


STATE_CHOICES = {
('andhra pradesh', 'andhra pradesh'),
}


class Customer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	locality = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	zipcode = models.IntegerField()
	state = models.CharField(choices=STATE_CHOICES, max_length=50)
	phoneNumber = models.PositiveIntegerField()

	def __str__(self):
		return str(self.name)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product') 
    
    def __str__(self):
        product_names = ', '.join([product.name for product in self.products.all()])
        return f"Cart for {self.user.username}: {product_names}"



STATUS_CHOICES = {
('ACCEPTED','ACCEPTED'),
('Packed','Packed'),
('On the Way','On the way'),
('Deliverd','Deliverd'),
('cancel','cancel'),
}
class OrderdItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50,default='Pending')
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


	

class Contact(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     message = models.TextField()
     def __str__(self):
	     return str(self.name)  
     


