from django.db import models


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=32)
	price = models.FloatField(max_length=10)
	description = models.CharField(max_length=250, default="No Decription Available")
	imgurl = models.ImageField(upload_to ='uploads/', default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")


class Cart(models.Model):
	productid = models.ForeignKey(Product, to_field='id',  null=False, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	custID = models.IntegerField()
