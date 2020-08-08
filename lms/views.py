from django.shortcuts import render,reverse
from lms.models import Course,Module,Lesson,CourseStatus
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect,JsonResponse

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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_course = CourseStatus.objects.get(user = self.request.user)
		viewed = [i.video_id for i in user_course.completed_lessons.all()]
		context['viewed'] = viewed
		context['view_count'] = len(viewed)
		return context

def onended(request):
	if request.is_ajax():
		iframe_id = request.GET.get('iframe_id')
		status = CourseStatus.objects.get(user = request.user)
		current_lesson = Lesson.objects.get(video_id = iframe_id)
		next_lesson = Lesson.objects.filter(id__gt=current_lesson.id).order_by('id').first()
		status.current_lesson = current_lesson
		status.completed_lessons.add(next_lesson)
		status.save()
		data = {'next':next_lesson.id,'get_slug':next_lesson.get_slug(),'percent':status.percent()}
	return JsonResponse(data)
