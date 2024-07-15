from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('environmental/',views.environmental,name='environmental'),
    path('announcements',views.announcements,name='announcements'),
    path('contact/',views.contact,name='contact'),
    path('announcements/<int:pk>/',views.announcement_detail,name='announcement_detail'),
    path('publications/',views.publications,name='publications'),


]