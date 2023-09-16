"""
URL configuration for mahendra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.get, name='products'),
    path('products/', views.post, name='products'),
    path('condideteList', views.my_view, name='conlist'),
    path('delete/<int:id>', views.Delete, name='delete'),
    path('update/<int:id>', views.Update, name='update'),
    path('update/uprce/<int:id>', views.uprce, name='uprce'),   
    path('addcompany', views.addcompany,name='addcompany'),
    path('Company-data-show',views.addcompany_data_show, name='company-data'),
    path('company_update/<int:id>', views.Company_list_update, name='company_update'),
    path('company_update/company_update/<int:id>', views.Company_update, name='company_update'), 
    path('Company-Dalete-Date/<int:id>', views.Company_Delete, name='Company-Dalete-Date'),
    # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    
    
    

   
        

]


#AdminName-Mahendar
#AdminPassword-12345