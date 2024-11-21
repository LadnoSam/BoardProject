from django.contrib import admin

# Register your models here.
from .models import Boardgame, Description, BorrowedGame

admin.site.register(Boardgame)
admin.site.register(Description)
admin.site.register(BorrowedGame) 
