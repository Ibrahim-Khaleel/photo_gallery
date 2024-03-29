from django.db import models

# Create your models here.

class Category(models.Model):   
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"
    

class Item(models.Model):
    item = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name_plural = "Items"

