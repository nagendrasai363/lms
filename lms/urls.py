from django.urls import path
from lms.views import index,about,course,blog,contact,event,cart,checkout,detail

app_name = 'lms'

urlpatterns = [
    path('',index,name = 'index'),
    path('about/',about,name = 'about'),
    path('course/',course.as_view(),name = 'course'),
    path('blog/',blog,name = 'blog'),
    path('contact/',contact,name = 'contact'),
    path('event/',event,name = 'event'),
    path('cart/',cart,name = 'cart'),
    path('checkout/',checkout,name = 'checkout'),
    path('detail/<slug:slug>/',detail.as_view(),name = 'detail'),
]