from django.db import models

# Create your models here.
class AddBook(models.Model):
    bookid = models.IntegerField()
    booktitle = models.CharField(max_length=120,null=True,blank=True)
    bookauth = models.CharField(max_length=120,null=True,blank=True)
    bookaval = models.CharField(max_length=120,null=True,blank=True)
    
def __str__(self):
    return self.bookid
