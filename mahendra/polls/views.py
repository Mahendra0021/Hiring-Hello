from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import CompanyModel,Company_Detail

from django.urls import reverse
from django.contrib import messages
from django.template import loader

# class Home(View):
#     def index(self, request):
#         return render(request,'home.html')
    
#     def get(self, request):
#         fm=CompanyModel()
#         return render(request, 'core/add-student.html',{'form':fm})
    
#     def post(self,request):
#         fm=CompanyModel(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/')
#         else:
#             return render(request, 'core/add-student.html',{'form':fm})
def get(request):
    return render(request,'index.html')

def post(request):
    print("mahendra")
    print(request.method)
    if request.method=='POST':
        name=request.POST.get('namee')
        condect=request.POST.get('Contacted')
        Current_company_name=request.POST.get('Current')
        location=request.POST.get('Location')
        Experience=request.POST.get('Experience')
        Cost=request.POST.get('Cost')
        ECTC=request.POST.get('Expected')
        Perrefered_job_location=request.POST.get('Perrefered') 
        Notic=request.POST.get('Notice')
        Linkedin_URL=request.POST.get('Linkedin')
        Communication=request.POST.get('Communication')
        Feedback=request.POST.get('Feedback') 
        File=request.POST.get('myfile') 
        print(name,condect)
       
        my_user = CompanyModel(
            name=name,
            condect=condect,
            Current_company_name=Current_company_name,
            location=location,
            Experience=Experience,
            Cost=Cost,
            ECTC=ECTC,
            Perrefered_job_location=Perrefered_job_location,
            Notic=Notic,
            Linkedin_URL=Linkedin_URL,
            Communication=Communication,
            Feedback=Feedback,
            File=File
        ) 
        my_user.save()
        return HttpResponse("your company detail created successfully")
    return render(request,'base.html') 
    #     teil=CompanyDetail.objects.all() 
    #     for a in teil:
    #         a.save()
    #         return HttpResponse("your company detail created successfully")
    
       
def my_view(request):
   con=CompanyModel.objects.all()
   for i in con:
    return render(request, 'candidate.html',{'company':con})
   
def Delete(request,id):
   print(id)
   a=CompanyModel.objects.get(pk=id)
   a.delete()
   
   return redirect('/condideteList')
def Update(request, id):
   mem=CompanyModel.objects.get(id=id)
   return render (request, 'update.html',{'mem':mem})
def uprce(request,id):
   name=request.POST['namee']
   condect=request.POST['Contacted']
   Current_company_name=request.POST['Current']
   location=request.POST['Location']
   Experience=request.POST['Experience']
   Cost=request.POST['Cost']
   ECTC=request.POST['Expected']
   Perrefered_job_location=request.POST['Perrefered'] 
   Notic=request.POST['Notice']
   Linkedin_URL=request.POST['Linkedin']
   Communication=request.POST['Communication']
   Feedback=request.POST['Feedback']
   File=request.POST['myfile']
   print(name,condect, Current_company_name ,location,Experience,Cost,ECTC,Perrefered_job_location,Notic,Linkedin_URL,Communication,Feedback,File)
   member = CompanyModel.objects.get(id=id)
   member.name=name
  
   member.condect=condect
   member.Current_company_name=Current_company_name
   member.location=location
   member.Experience=Experience
   member.Cost=Cost
   member.ECTC=ECTC
   member.Perrefered_job_location=Perrefered_job_location
   member.Notic=Notic
   member.Linkedin_URL=Linkedin_URL
   member.Communication=Communication
   member.Feedback=Feedback
   member.File=File
   member.save()
   return HttpResponseRedirect('/')
   
def addcompany(request):
   if request.method=='POST':
      Cname=request.POST.get('Cname')
      C_contact=request.POST.get('C_contact')
      CEmail=request.POST.get('CEmail')
      Caddress=request.POST.get('Caddress')
      City=request.POST.get('City')
      CWebsite=request.POST.get('CWebsite')
      CLinkedin_URL=request.POST.get('CLinkedin_URL')
      CDetail=Company_Detail(
      Cname=Cname,
      C_contact=C_contact,
      CEmail=CEmail,
      Caddress=Caddress,
      City=City,
      CWebsite=CWebsite,
      CLinkedin_URL=CLinkedin_URL
      )
      CDetail.save()
      return HttpResponse("your company detail created successfully")
   return render(request,'addcompany.html')
def addcompany_data_show(request):
   con=Company_Detail.objects.all()
   for i in con:
    return render(request, 'addcompany_data_show.html',{'addcompany':con})
def Company_list_update(request, id):
   i=Company_Detail.objects.get(id=id)
   return render (request, 'Company_list_update.html',{'i':i})

def Company_update(request,id):
   Cname=request.POST['Cname']
   C_contact=request.POST['C_contact']
   CEmail=request.POST['CEmail']
   Caddress=request.POST['Caddress']
   City=request.POST['City']
   CWebsite=request.POST['CWebsite']
   CLinkedin_URL=request.POST['CLinkedin_URL']
   print(Cname,C_contact,CEmail,Caddress,City,CWebsite,CLinkedin_URL)
   member = Company_Detail.objects.get(id=id)
   member.Cname=Cname
   member.C_contact=C_contact
   member.CEmail=CEmail
   member.Caddress=Caddress
   member.City=City
   member.CWebsite=CWebsite
   member.CLinkedin_URL=CLinkedin_URL
   member.save()
   return HttpResponseRedirect('/')
def Company_Delete(request,id):
   print(id)
   a=Company_Detail.objects.get(pk=id)
   a.delete()
   
   return redirect('/Company-data-show')




# def Update(request,id):
#    data=CompanyModel.objects.get(id=id)
#    template= loader.get_template('base.html')
#    context={
#       'data':data,
#    }
#    return HttpResponse(template.render(context,request))
# def updaterecord(request, id):
#    name=request.POST['namee']
#    condect=request.POST['Contacted']
#    Current_company_name=request.POST['Current']
#    location=request.POST['Location']
#    Experience=request.POST['Experience']
#    Cost=request.POST['Cost']
#    ECTC=request.POST['Expected']
#    Perrefered_job_location=request.POST['Perrefered'] 
#    Notic=request.POST['Notice']
#    Linkedin_URL=request.POST['Linkedin']
#    Communication=request.POST['Communication']
#    Feedback=request.POST['Feedback']
#    File=request.POST['myfile']
#    print(name,condect, Current_company_name ,location,Experience,Cost,ECTC,Perrefered_job_location,Notic,Linkedin_URL,Communication,Feedback,File)
#    member = CompanyModel.objects.get(id=id)
#    member.name=name
  
#    member.condect=condect
#    member.Current_company_name=Current_company_name
#    member.location=location
#    member.Experience=Experience
#    member.Cost=Cost
#    member.ECTC=ECTC
#    member.Perrefered_job_location=Perrefered_job_location
#    member.Notic=Notic
#    member.Linkedin_URL=Linkedin_URL
#    member.Communication=Communication
#    member.Feedback=Feedback
#    member.File=File
#    member.save()
#    return HttpResponseRedirect('/')
   


#    if request.method=='POST':
#         name=request.POST.get('namee')
#         condect=request.POST.get('Contacted')
#         Current_company_name=request.POST.get('Current')
#         location=request.POST.get('Location')
#         Experience=request.POST.get('Experience')
#         Cost=request.POST.get('Cost')
#         ECTC=request.POST.get('Expected')
#         Perrefered_job_location=request.POST.get('Perrefered') 
#         Notic=request.POST.get('Notice')
#         Linkedin_URL=request.POST.get('Linkedin')
#         Communication=request.POST.get('Communication')
#         Feedback=request.POST.get('Feedback') 
#         File=request.POST.get('myfile') 
#         print(name,condect)
       
#         my_user = CompanyModel(
           
#             name=name,
#             condect=condect,
#             Current_company_name=Current_company_name,
#             location=location,
#             Experience=Experience,
#             Cost=Cost,
#             ECTC=ECTC,
#             Perrefered_job_location=Perrefered_job_location,
#             Notic=Notic,
#             Linkedin_URL=Linkedin_URL,
#             Communication=Communication,
#             Feedback=Feedback,
#             File=File
#         )
        # my_user.save() 
        


