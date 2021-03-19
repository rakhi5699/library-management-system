from django.contrib import admin
from . models import AddBook
# Register your models here.
class AddBookAdmin(admin.ModelAdmin):
    list_display=('bookid','booktitle','bookauth','bookaval')
    list_filter=('bookaval',)
    list_editable=('bookaval',)


admin.site.register(AddBook,AddBookAdmin)

