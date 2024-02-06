from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.title


class Microcontoller(models.Model):
    title = models.CharField(max_length = 300)
    mcu_qty = models.IntegerField()
    #category = models.ForeignKey(Category,on_delete = models.CASCADE)
    #created_at = models.DateField(default=timezone.now)
    #user = models.ForeignKey(User,verbose_name = 'Ueser',on_delete =  models.CASCADE)

    def __str__(self) -> str:
        return self.title