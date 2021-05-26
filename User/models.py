from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class all_user(models.Model):
	name = models.CharField(max_length=50)
	dob = models.DateField()
	email = models.EmailField(unique=True)
	phone_no = PhoneNumberField(unique=True)

	class Meta:
		verbose_name="User"

	def __str__(self):
		return self.name