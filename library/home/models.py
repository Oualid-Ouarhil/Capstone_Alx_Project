from django.db import models

class book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.CharField(max_length= 100)
    isbn = models.CharField(max_length=13, unique=true)
    published_date = models.DateField()
    copies_available = models.PositiveIntergerField()

    def __str__(self):
        return self.title

class user(models.Model):
    username = models.CharField(max_length=150, unique=true)
    email = models.EmailField(unique=true)
    date_of_membership = models.DateField(auto_now_add=true)
    is_active = models.BooleanField(default=true)

    def __str__(self):
        return self.username
