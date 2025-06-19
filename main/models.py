from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email manzilingiz")
    subject = models.CharField(max_length=255, verbose_name="Mavzu")
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"