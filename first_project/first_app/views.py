from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
from . import forms

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'index.html',context=date_dict)
    
               
def index_form(request):
    return render(request,'basic_app/index_form.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'basic_app/form.html',{'form':form})
