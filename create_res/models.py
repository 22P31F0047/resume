from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=250)
    middlename=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    dob = models.DateField()
    emailaddress=models.EmailField(max_length=250)
    gender=models.CharField(max_length=30,default="no")
    user_name=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    confirmpassword=models.CharField(max_length=250)

    def _str_(self):
        return self.user_name


class update_details(models.Model):
    resume = models.ForeignKey('register', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_obj=models.CharField(max_length=500)
    mob_no=models.IntegerField()
    skills=models.CharField(max_length=250)
    projects=models.CharField(max_length=250)
    tools=models.CharField(max_length=250)
    achievements=models.CharField(max_length=250)
    lan_knw=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    
    def _str_(self):
        return self.skills

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey('register', on_delete=models.CASCADE)
    DEGREE_CHOICES = (
        ('high_school', 'High School'),
        ('intermediate', 'Intermediate'),
        ('bachelors', 'Bachelor\'s'),
        ('masters', 'Master\'s'),
        ('phd', 'PhD'),
    )
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES)
    institution = models.CharField(max_length=255)
    cgpa=models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.degree

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey('register', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def _str_(self):
        return self.title
    