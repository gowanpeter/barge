from django.contrib import admin
from django.db import models
from .models import Piece

# Register your models here.
class PieceAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Piece, PieceAdmin)
