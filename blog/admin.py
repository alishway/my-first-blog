from django.contrib import admin
from .models import Post

admin.site.register(Post)
# we need to register the model with admin.site.register(Post).
