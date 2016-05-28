from django.db import models

class Student(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	year_graduation = models.IntegerField()

	def __str__(self):
		return self.first_name+" "+self.last_name

class Service_Classification(models.Model):
	class_name = models.TextField()

	def __str__(self):
		return self.class_name

class Service(models.Model):
	service_classification = models.ForeignKey(Service_Classification)
	service_name=models.TextField()
	agency = models.TextField()
	street = models.TextField()
	city = models.TextField()
	state = models.TextField()
	zipcode=models.TextField()
	country = models.TextField()
	url = models.TextField()
	contact_phone = models.TextField()
	contact_name = models.TextField()
	contact_email = models.TextField()
	contact_address = models.TextField()

class Service_Activiy(models.Model):
	service = models.ForeignKey(Service)
	student = models.ForeignKey(Student)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	hours = models.IntegerField
	activiy_detail = models.TextField()
	contact = models.TextField()
	submitdate = models.DateField()
