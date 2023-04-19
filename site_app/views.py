from django.shortcuts import render

def home(request):
    return render(request,'site_app/index.html',{})

def about(request):
    return render(request,'site_app/about.html',{})

def blog(request):
    return render(request,'site_app/blog.html',{})

def contact(request):
    return render(request,'site_app/contact.html',{})

def detail(request):
    return render(request,'site_app/detail.html',{})

def feature(request):
    return render(request,'site_app/feature.html')

def quote(request):
    return render(request,'site_app/quote.html',{})

def service(request):
    return render(request,'site_app/service.html',{})

def team(request):
    return render(request,'site_app/team.html',{})

def testimonial(request):
    return render(request,'site_app/testimonial.html',{})