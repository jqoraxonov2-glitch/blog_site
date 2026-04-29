from django.contrib import admin
from .models import Post

# admin ni o'gartishish uchun yozilgan decorator

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # admin uchun imtiyozlar
    list_display = ('title', 'slug', 'author', 'publish', 'status') # postlar ro'yxatida ko'rinadiganlar
    list_filter = ('status', 'created', 'publish', 'author') # filter
    search_fields = ('title', 'body') # poisk qismi
    prepopulated_fields = {'slug': ('title', )} # avvaldan hisoblangan fieldlar #admin qo'ygan titleni
    # slugni o'zi qo'yib beradi
    raw_id_fields = ('author', ) # Admin panelda ko'rinadi
    date_hierarchy = 'publish' # sana bo'yicha erarhiya
    ordering = ('status', 'publish') # qoida si statusi publish bo'lganlarnigina olsin
