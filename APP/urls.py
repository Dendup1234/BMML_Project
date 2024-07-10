from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('environmental/',views.environmental,name='environmental'),
    path('announcements',views.announcements,name='announcements'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name ='news'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
    path('announcements/<int:pk>/',views.announcement_detail,name='announcement_detail'),
    path('publications/',views.publications,name='publications')

]