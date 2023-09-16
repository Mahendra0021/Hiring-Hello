from django.contrib import admin
from polls.models import CompanyModel,Company_Detail
# Register your models here.
class Companyadmin(admin.ModelAdmin):
    list_display=('name','condect','Current_company_name','location','Experience','Cost','ECTC','Perrefered_job_location','Notic','Linkedin_URL','Communication','Feedback','File',)

admin.site.register(CompanyModel,Companyadmin)


class Companydateiladmin(admin.ModelAdmin):
    list1=('Cname','C_contact','CEmail','Caddress','City','CWebsite','CLinkedin_URL')

admin.site.register(Company_Detail,Companydateiladmin)