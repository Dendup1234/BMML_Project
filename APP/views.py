from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    home = Homepage.objects.all()
    stats = Statistic.objects.all()
    latest_news = News.objects.order_by('-date')[:3]
    context ={
        'home': home,
        'stat': stats,
        'news': latest_news
    }
    return render (request,'index.html',context)

def news(request):
    news = News.objects.all()
    context ={
        'news': news,
    }
    return render(request,'news.html',context)

def news_detail(request, pk):
    news = get_object_or_404(News, id=pk)
    context ={
        'news': news,
    }
    return render(request, 'news_detail.html', context)

def about(request):
    home = Homepage.objects.all()
    stats = Statistic.objects.all()
    raw = Raw_material.objects.all()
    team = Team_Member.objects.all()
    board_team = Team_Member.objects.filter(Q(role='Head Officer') | Q(role='CEO') | Q(role='Manager'))
    context ={
        'home': home,
        'stats': stats,
        'raw': raw,
        'team': team,
        'board': board_team,
    }
    return render (request,'about.html',context)

def environmental(request):
    certificates = Certificates.objects.all()
    context ={
        'certificates': certificates
    }
    return render (request,'environmental.html',context)

def products(request):
    return render (request,'product.html')

def announcements(request):
    career = Career.objects.all()
    announcement = Announcement.objects.all()
    context ={
        'career': career,
        'announcement': announcement,
    }
    return render (request,'announcements.html',context)

def announcement_detail(request,pk):
    announcements = get_object_or_404(Announcement, pk=pk)
    context ={
        'announcement': announcements,
    }
    return render (request,'announcement_details.html',context)

def contact(request):
    team = Team_Member.objects.all()
    context ={
        'team': team,
    }
    return render (request,'contact.html',context)

def publications(request):
    report = Reports.objects.all()
    context ={
        'report' : report,

    }
    return render (request,'publications.html',context)
