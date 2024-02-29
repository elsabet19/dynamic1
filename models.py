from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Why(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
     return self.title
    
class Homemotto(models.Model):
      title = models.CharField(max_length=200)
      titlee = models.CharField(max_length=200)
      motto = RichTextField()

      def __str__(self):
        return self.title


class Homecard(models.Model):
   title = models.CharField(max_length=200)
   description = RichTextField()
   
   def __str__(self):
      return self.title

class Homepopular(models.Model):
   image= models.ImageField()
   type = models.CharField(max_length=100)
   money = models.CharField(max_length=30)
   title = models.CharField(max_length=200)
   description = RichTextField()
   personimage = models.ImageField(blank=True)
   personname = models.CharField(max_length=200)

   def __str__(self):
      return self.title
   
class Mentor(models.Model):
   image= models.ImageField()
   name = models.CharField(max_length=200)
   type=models.CharField(max_length=100)
   description = RichTextField()
   twitter = models.URLField()
   facebook = models.URLField()
   instagram = models.URLField()
   linkedin = models.URLField()

   def __str__(self):
      return self.name
   
class About(models.Model):
   image = models.ImageField()
   title = models.CharField(max_length=200)
   description = RichTextField()
   student = models.IntegerField()
   course = models.IntegerField()
   event = models.IntegerField()
   trainers = models.IntegerField()
   
   def __str__(self):
      return self.title
   
class Abouttestimony(models.Model):
   image = models.ImageField()
   name = models.CharField(max_length=200)
   title = models.CharField(max_length=200)
   testimony = RichTextField()

   def __str__(self):
      return self.title


   
class Trainers(models.Model):
   image = models.ImageField()
   name = models.CharField(max_length=200)
   type = models.CharField(max_length=100)
   description = RichTextField()
   twitter = models.URLField()
   facebook = models.URLField()
   instagram = models.URLField()
   linkedin = models.URLField()

   def __str__(self):
      return self.name
   
class Events(models.Model):
   image = models.ImageField()
   title = models.CharField(max_length=200)
   date = models.DateTimeField()      #check datatype
   description = RichTextField()

   def __str__(self):
      return self.title
   
class Pricing(models.Model):
   title = models.CharField(max_length=200)
   money = models.CharField(max_length=30)
   description = RichTextField()

   def __str__(self):
      return self.title
   
class Courses(models.Model):
   image= models.ImageField()
   type = models.CharField(max_length=100)
   money =models.CharField(max_length=30)
   title = models.CharField(max_length=200)
   description = RichTextField()
   personimage = models.ImageField(blank=True)
   personname = models.CharField(max_length=200,blank=True)
   trainer = models.CharField(max_length=200,blank=True)
   money2 = models.CharField(max_length=30,blank=True)
   seats = models.IntegerField(blank=True)
   schedule = models.CharField(max_length=30,blank=True)

   def __str__(self):
      return self.title
   '''
class Coursedetails(models.Model):
     image = models.ImageField()
     title = models.CharField(max_length=200)
     description = RichTextField()
     trainer = models.CharField(max_length=200)
     money = models.CharField(max_length=30)
     seats = models.IntegerField()
     schedule = models.CharField(max_length=30)

     def __str__(self):
      return self.title'''
     


class FooterMentor(models.Model):
   street = models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   country = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   email  = models.EmailField()
  
   def __str__(self):
      return self.email

class Footersoci(models.Model):
   twitter = models.CharField(max_length=200)
   facebook = models.CharField(max_length=200)
   instagram = models.CharField(max_length=200)
   linkedin = models.CharField(max_length=200)
 
  
   def __str__(self):
      return self.email

class ContactInformation(models.Model):
   
   address = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   email  = models.EmailField()
  


   def __str__(self):
      return self.email
   
   
class ContactMessage(models.Model):
   name  = models.CharField(max_length = 200)
   email  =  models.EmailField()
   subject  = models.CharField(max_length=200)
   message = models.TextField()
   
   def __str__(self):
      return self.name+"name"