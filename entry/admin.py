from django.contrib import admin
from .models import Entry, EntryEmbedding

# Register your models here.
admin.site.register(Entry)
admin.site.register(EntryEmbedding)