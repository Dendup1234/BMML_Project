from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.

def base(request):
    admin = Admin_info.objects.all()
    context={
        'admin':admin,
    }
    return(request,'base.html',context)


def index(request):
    home = Homepage.objects.all()
    stats = Statistic.objects.all()
    context ={
        'home': home,
        'stat': stats,
    }
    return render (request,'index.html',context)

def about(request):
    home = Homepage.objects.all()
    stats = Statistic.objects.all()
    raw = Raw_material.objects.all()
    team = Team_Member.objects.all()
    certificates = Certificates_about.objects.all()
    context ={
        'home': home,
        'stats': stats,
        'raw': raw,
        'team': team,
        'certi': certificates,
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
    tender = Tenders.objects.all()
    context ={
        'career': career,
        'announcement': announcement,
        'tender':tender,
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
    tenders = Annual_Audited_Reports.objects.all()
    context ={
        'report' : report,
        'Annual': tenders,

    }
    return render (request,'publications.html',context)
