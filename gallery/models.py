from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
class Category(models.Model):
    name=models.CharField(max_length=120)

    class Meta:
        ordering=['-name']
        verbose_name_plural='Categories'

    def __str__(self):
        return f'{self.name}'

class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='photos')
    name=models.CharField(max_length=120)
    slug=models.SlugField(max_length=120)
    description=models.TextField()
    image=models.ImageField(upload_to='image/%Y/%m/%d')
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        indexes=[
            models.Index(fields=['-created_at']),
        ]

    def save(self, *args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])
