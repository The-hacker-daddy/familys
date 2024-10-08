from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  correo = models.CharField(max_length=255, null = True, blank=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  direccion = models.CharField(max_length=255, null = True)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

