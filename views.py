from django.shortcuts import render,redirect
from .models import Why,Homecard,Mentor,Abouttestimony,Courses,About,Trainers,Events,Pricing,ContactMessage,ContactInformation,Homemotto,FooterMentor,Footersoci
#import telegram
#import asyncio

def home(request):
   why = Why.objects.all().first()
   mottoo = Homemotto.objects.all().first() 
   card = Homecard.objects.all()
   mentor = Mentor.objects.all()
   data = {'why_data':why,'motto_dataa':mottoo,'card_data':card,'mentor_data':mentor}
   return render(request, 'home.html',data)



'''
def homecard(request):
   
   data = {}
   return render(request, 'home.html',data)
'''
'''
def homecourse(request):
   course=Homepopular.objects.all()
   data={'course_data':course}
   return render(request, 'home.html',data)'''
'''
def mentors(request):
   mentor=Mentor.objects.all()
   data={'mentor_data':mentor}
   return render(request, 'home.html',data)'''

def about(request):
   about=About.objects.all().first()
   testimony=Abouttestimony.objects.all()
   data={'about_data':about,'testimony_data':testimony}
   return render(request,'about.html',data)
'''
def testimonys(request):
   
   data={}
   return render(request, 'about.html',data)'''

def course(request):
   course=Courses.objects.all()
   data={'courses_data':course}
   return render(request, 'courses.html',data)

def coursedetails(request,post_id):
    #detail=Coursedetails.objects.all()
    # data={'details_data':detail}
 #  return render(request, 'coursedetails.html',{'coursedetails.html':data},data)
   course=Courses.objects.get(id = post_id)
   return render(request, 'coursedetails.html',{'courses_data':course})
  

def pricing(request):
   price=Pricing.objects.all()
   data={'price_data':price}
   return render(request, 'pricing.html',data)

def trainers(request):
   trainer=Trainers.objects.all()
   data={'trainers_data':trainer}
   return render(request, 'trainers.html',data)

def events(request):
   event=Events.objects.all()
   data={'events_data':event}
   return render(request, 'events.html',data)



def footer(request):
   foot=FooterMentor.objects.all().first()
   foots=Footersoci.objects.all()
   data={'footer_data':foot,'social_data':foots}
   return render(request,'footer.html','home.html',data)
'''
def footersoc(request):
   
   data={}
   return render(request,'footer.html',data)'''

def contact_us(request):
   info = ContactInformation.objects.all().first()
   
   if request.method == 'POST':
      
      name1  = request.POST.get('name')
      email1  = request.POST.get('email')
      subject1  = request.POST.get('subject')
      message1  = request.POST.get('message')
      
      contact = ContactMessage()
      contact.name = name1
      contact.email = email1
      contact.subject = subject1
      contact.message =message1
      
      contact.save()
         
      
   return render(request, 'contact.html',{'info':info}) 

'''
def contact_us(request):
   info = ContactInformation.objects.all().first()
   contact_data={'contact_data':info}

   
   if request.method == 'POST':
      
      name1  = request.POST.get('name')
      email1  = request.POST.get('email')
      subject1  = request.POST.get('subject')
      message1  = request.POST.get('message')
      
      contact = ContactMessage()
      
      contact.name = name1
      contact.email = email1
      contact.subject = subject1
      contact.message =message1
      
      contact.save()
         
      dataTg=[
         {'name':name1,'detail':'email'+email1+''+'subject'+subject1+''+'message'+message1}
      ]
      sendData(dataTg)
      
   return render(request, 'contact.html',contact_data)

def sendData(dataT):
   bot_token="5810719434:AAFU43cnz9DzBl9s8R-Ino3RHbflIjPzW70"
   channel_id='-1001826934314'
   bot=telegram.Bot(token=bot_token)
   async def send_messages():
        for item in dataT:
            message = f"{item['name']}:\n{item['detail']}"
            await bot.send_message(chat_id=channel_id, text=message)

    # Call the async function to send the messages
   asyncio.run(send_messages()) '''