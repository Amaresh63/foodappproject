from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000,default='https://t3.ftcdn.net/jpg/04/17/41/92/360_F_417419275_y8vQY8TXGRpQGpsgkkqihUaWpmtukRhY.jpg')
 