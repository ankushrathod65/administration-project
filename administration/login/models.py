from django.db import models

# Create your models here.
class tbl_Authentication(models.Model):
    Empcode=models.IntegerField()
    Username=models.CharField(max_length=50,default='')
    Password=models.CharField(max_length=50,default='')
    is_active=models.IntegerField(null=True)

    def __str__(self):
        return self.username

    empAuth_objects=models.Manager()
# from django.db import connection
# c=connection.cursor()