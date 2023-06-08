from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.html import format_html

import uuid



class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(default="", null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args, **kwargs)


class BooksModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    blob = models.TextField()
    book_image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    genre = models.ManyToManyField('Tag', blank=True, related_name='tags')
    posted_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    slug = models.SlugField(default='', null=False)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def manytomany(self):
        return format_html(
            '<span style="color: #{};>{}{}</span>',
            self.genre
        )

    def __str__(self) -> str:
        return self.name 
    
    def get_absolute_url(self):
        return reverse('bookdetails', kwargs={"slug": self.slug})



class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    tag = models.CharField(max_length=200, null=True)
    slug = models.SlugField(default="", null=False, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = ['id', 'slug']

    def __str__(self) -> str:
        return self.tag

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args, **kwargs)
    
