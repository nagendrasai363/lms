from django.shortcuts import render
from lms.models import Course
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about-us.html')

class course(ListView):
	model = Course
	template_name = 'course.html'

def blog(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')

def event(request):
	return render(request,'event.html')

def cart(request):
	return render(request,'cart.html')

def checkout(request):
	return render(request,'checkout.html')

class detail(DetailView):
	model = Course
	template_name = 'course_detail.html'
