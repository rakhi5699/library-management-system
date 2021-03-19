from django.urls import path
from . views import home,add,delet,issue,returnbook,view

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('delete/',delet,name='delete'),
    path('issue/',issue,name='issue'),
    path('returnbook/',returnbook,name='returnbook'),
    path('view/',view,name='view'),
]