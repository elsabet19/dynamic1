from django.urls import path, include
from .views import home,about,contact_us,coursedetails,events,pricing,trainers,course,footer
urlpatterns = [

   path('', home, name="home_url"),
   path('about/',about, name='about_url'),
   path('contact/',contact_us, name='contact_url'),
   path('events/',events, name='events_url'),
   path('pricing/',pricing, name='pricing_url'),
   path('trainers/',trainers, name='trainers_url'),
   path('courses/',course, name='courses_url'),
   path('coursedetails/<int:post_id>/',coursedetails, name='coursedetails_url'),
   path('footer/',footer,name='footer_url')
   
]