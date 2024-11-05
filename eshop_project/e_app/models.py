from django.db import models


# Create your models here.
class Product(models.Model):
    product_id=models.TextField()
    product_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()

# class Buy(models.Model):
#     user=models.ForeignKey(User,on_delete.CASCADE)
#     Product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     price=models.IntegerField()
#     date=models.DateField(auto_now_add=True)

