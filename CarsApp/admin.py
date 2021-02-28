from django.contrib import admin
# from . models import Log,PostImage
from .models import *

# Register your models here.

# class PostImageAdmin(admin.StackedInline):
#     model=PostImage

# @admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     inlines=[PostImageAdmin]

#     class Meta:
#         model=Log

# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

admin.register(Login)
admin.register(Car)
admin.register(CarBrand)
admin.register(CarImages)
admin.register(CarModel)