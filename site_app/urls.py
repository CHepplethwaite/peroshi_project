from django.urls import path
from . import views as site_app_views

urlpatterns = [
    path('',site_app_views.home, name="home"),
    path('about/',site_app_views.about, name="about"),
    path('blog/',site_app_views.blog, name="blog"),
    path('contact/',site_app_views.contact, name="contact"),
    path('detail/',site_app_views.detail, name="detail"),
    path('feature/',site_app_views.feature, name="feature"),
    path('quote/',site_app_views.quote, name="quote"),
    path('service',site_app_views.service, name="service"),
    path('team', site_app_views.team, name="team"),
    path('testimonial', site_app_views.testimonial, name="testimonial"),
]