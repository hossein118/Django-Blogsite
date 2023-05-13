from django.db import models
from django.utils.html import format_html
from django.utils.timezone import now
from extensions.utils import jalali_converter
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    position = models.IntegerField()
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    STATUS_CHOICES = (
        ('p','published'),
        ('d','draft')
    )
    title = models.CharField(max_length=90)
    body = models.TextField()
    category = models.ManyToManyField(Category,related_name='blogs')
    publish = models.DateTimeField(default=now) 
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def thumbnail(self):
        return format_html("<img height=70 src='{}'>".format(self.image.url))

    def __str__(self) -> str:
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ"