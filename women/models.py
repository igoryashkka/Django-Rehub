from django.db import models
from django.urls import reverse

# Create your models here.
#Filed id is already included (Model)
class Women(models.Model):
    slug = models.SlugField(max_length = 255, unique = True,db_index = True,verbose_name = 'URL')
    title = models.CharField(max_length = 255,verbose_name = 'name title')
    content = models.TextField(blank = True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    time_created = models.DateTimeField(auto_now_add = True)
    time_updated = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default = True)
    #                       can paste just Category, without ''
    cat = models.ForeignKey('Category',on_delete = models.PROTECT,null = True)

    def __str__(self) -> str:
        return self.title
    # if we use exact get_absolute_url it will create "*view on site*" in admin panel
    def get_absolute_url(self):
        return reverse('post',kwargs={'slug':self.slug})
    
    class Meta:
        verbose_name = 'Popular womens'
        verbose_name_plural = 'Popular womens'
        ordering = ['time_created','-title']

    
class Category(models.Model):
    name = models.CharField(max_length = 255, db_index = True,verbose_name = 'NameCat')
    slug = models.SlugField(max_length = 255, unique = True,db_index = True,verbose_name = 'URL')
    def __str__(self) -> str:
        return self.name
    # if we use exact get_absolute_url it will create "*view on site*" in admin panel
    def get_absolute_url(self):
        return reverse('cat',kwargs={'cat_id':self.pk})
    

    class Meta:
        ordering = ['-id']
        verbose_name = 'NAME'
        verbose_name_plural = 'Names'
