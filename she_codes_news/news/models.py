from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone 

class Category(models.Model):
    title = models.CharField(max_length=100)

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = "stories"
    )
    category = models.ForeignKey(Category, null=True, on_delete = models.PROTECT)
    slug_field = models.SlugField(null=True, max_length=100, unique=True)

    def __str__(self):
        return self.title
