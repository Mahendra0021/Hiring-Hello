from django.db import models

from django.contrib.auth.models import UserManager
# Create your models here.
class CompanyModel(models.Model):
    name= models.CharField(max_length=100)
    condect= models.IntegerField(blank=True, null=True)
    Current_company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    Experience= models.CharField(max_length=100)
    Cost = models.IntegerField()
    ECTC= models.IntegerField()
    Perrefered_job_location= models.CharField(max_length=500)
    Notic= models.CharField(max_length=500)
    Linkedin_URL=models.CharField(max_length=400)
    Communication=models.CharField(max_length=500)
    Feedback=models.CharField(max_length=500)
    File=models.FileField(upload_to ='uploads/')
 
class CompanyDetail(models.Model):
    company_name=models.CharField(max_length=255, null=False)
    company_Update=models.CharField(max_length=100)
    ScreenRate=models.IntegerField()


class Company_Detail(models.Model):
    Cname= models.CharField(max_length=50)
    C_contact= models.IntegerField(blank=True, null=True)
    CEmail = models.EmailField(max_length=200, null=False)
    Caddress = models.CharField(max_length=500)
    City= models.CharField(max_length=500)
    CWebsite = models.CharField(max_length=400)
    CLinkedin_URL=models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.Cname   
# class conlist(models.Model):
#     name = models.CharField(max_length=100)
#     CompanyName =  models.CharField(max_length=100)
#     Experience= models.CharField(max_length=100)
#     position= models.CharField(max_length=100)