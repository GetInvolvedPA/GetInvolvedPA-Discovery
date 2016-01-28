from django.db import models

class Student(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	year_graduation = models.IntegerField()

class Service_Classification(models.Model):
	class_name = models.TextField()

class Service(models.Model):
	service_id = models.IntegerField()
	service_class_id = models.ForeignKey(Service_Classification)
	serviceName=models.TextField()
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
	activiy_id = models.IntegerField()
	service_id = models.ForeignKey(Service)
	student = models.ForeignKey(Student)

	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	hours = models.IntegerField
	activiy_detail = models.TextField()
	contact = models.TextField()
	submitdate = models.DateField()
