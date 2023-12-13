from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return "Rasim"


class Timeline(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="timeline/")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)

    def __str__(self):
        return "Contact Information"

