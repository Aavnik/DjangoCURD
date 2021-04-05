from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_age = models.IntegerField()
    user_email = models.EmailField(max_length=150)
    user_password = models.CharField(max_length=10)
    

    def __str__(self):
        return self.user_name
