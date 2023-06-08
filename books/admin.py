from django.contrib import admin
from .models import Author, Tag, BooksModel


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'blob', 'book_image', 'posted_on', 'price', 'slug']
    list_display_links = ['name', 'author']

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(BooksModel, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Author, AuthorAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug']
    list_display_links = ['tag']

    prepopulated_fields = {"slug": ("tag",)}


admin.site.register(Tag, TagAdmin)