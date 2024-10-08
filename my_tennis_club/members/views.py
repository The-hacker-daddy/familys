from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
    mymember = Member.objects.get(id=id)
    phone = f"{mymember.phone:010d}"
    context = {
        'mymember': mymember,
        'phone': phone, 
    }
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
    'mymembers': mymembers,   
    }
    return HttpResponse(template.render(context, request))