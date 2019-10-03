from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

def gen_slug(s):                                                 #для генерации автаматического слага
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))                     #не обязательныo         

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug' : self.slug})

    def __str__(self):
        return f"{self.title}"

# Create your models here.
