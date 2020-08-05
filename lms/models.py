from django.db import models

# Create your models here.

class Course(models.Model):
	title = models.CharField(max_length = 100)
	short_description = models.TextField()
	description = models.TextField()
	img1240x600 = models.ImageField(upload_to = '')
	img293x274 = models.ImageField(upload_to = '')
	duration = models.CharField(max_length = 10)
	credits = models.IntegerField()
	reviews = models.FloatField()
	enrolled = models.IntegerField()
	slug = models.SlugField()
	offer_price = models.FloatField()
	original_price = models.FloatField()


	def __str__(self):
		return self.title

class Module(models.Model):
	course = models.ForeignKey(Course,on_delete = models.CASCADE)
	module = models.CharField(max_length = 1000)
	
	def __str__(self):
		return self.module

class Lesson(models.Model):
	module = models.ForeignKey(Module,on_delete = models.CASCADE)
	lesson = models.CharField(max_length = 1000)
	link = models.URLField()
	video_id = models.CharField(max_length = 11,default = '')

	def __str__(self):
		return self.lesson