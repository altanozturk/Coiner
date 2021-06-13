from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 200 , null = True)
	username = models.CharField(max_length = 200 , null = True)
	password = models.CharField(max_length = 20 , null = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)


	def __str__(self):
		return self.name

class Stock(models.Model):
	name = models.CharField(max_length = 200 , null = True)
	code = models.CharField(max_length = 200 , null = True)
	price = models.FloatField(null = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)
	


	def __str__(self):
		return self.name


class Buy(models.Model):
	STATUS = (
		('Sold' , 'Sold'),
		('Pending' , 'Pending'),
		('Receipt' , 'Receipt')
		)

	user = models.ForeignKey(User , null = True , on_delete = models.SET_NULL)
	stock = models.ForeignKey(Stock , null = True , on_delete = models.SET_NULL)
	status = models.CharField(max_length = 200 , null = True , choices = STATUS)
	date_created = models.DateTimeField(auto_now_add = True , null = True)

	def __str__(self):
		return self.stock.name



class Employee(models.Model):
	name = models.CharField(max_length = 200 , null = True)
	username = models.CharField(max_length = 200 , null = True)
	password = models.CharField(max_length = 20 , null = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)
	
	


	def __str__(self):
		return self.name

class Forum(models.Model):
	STATUS = (
		('Open' , 'Open'),
		('Closed' , 'Closed')
		)
	
	title = models.CharField(max_length = 200 , null = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)
	user = models.ForeignKey(User , null = True , on_delete = models.SET_NULL)
	employee = models.ForeignKey(Employee , null = True , on_delete = models.SET_NULL)
	status = models.CharField(max_length = 200 , null = True , choices = STATUS)



	def __str__(self):
		return self.title








	