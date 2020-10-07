from django.shortcuts import render
from .models import Cloth
from .forms import ContactForm
# Create your views here.
def index(request):
    cloths = Cloth.objects.all()
    form = ContactForm(request.POST or None)
    title = 'Contact'
    confirm_message = None
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'title': title , 
        'confirm_message':confirm_message,
        'form':form
        }
    if form.is_valid():
        name = form.cleaned_data['Name']
        comment = form.cleaned_data['Comment']
        subject = 'Message from WOW-burger.com'
        message = '%s %s'%(comment, name)
        emailForm = form.cleaned_data['Email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailForm, emailTo, fail_silently=False)
    return render(request, 'app/index.html', context)

def contact(request):
    title = "Thanks!"
    confirm_message = "Thanks for the message. We will get right back to you."
    form = None
    context = {'title': title , 'confirm_message':confirm_message, 'form':form}
    return render(request, 'app/contact.html', context)

def temp(request):
    cloths = Cloth.objects.all()
    context = {
        'cloths':cloths,
        }
    return render(request, 'app/temp.html', context)

def jeans(request):
    cloths = Cloth.objects.filter(tag='Jeans')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Jeans',
        }
    return render(request, 'app/jeans.html', context)

def shirts(request):
    cloths = Cloth.objects.filter(tag='Shirts')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Shirts',
        }
    return render(request, 'app/shirts.html', context)

def gymwear(request):
    cloths = Cloth.objects.filter(tag='Gymwear')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Gymwear',
        }
    return render(request, 'app/gymwear.html', context)

def shoes(request):
    cloths = Cloth.objects.filter(tag='Shoes')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Shoes',
        }
    return render(request, 'app/shoes.html', context)

def jackets(request):
    cloths = Cloth.objects.filter(tag='Jackets')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Jackets',
        }
    return render(request, 'app/jackets.html', context)

def dresses(request):
    cloths = Cloth.objects.filter(tag='Dresses')
    context = {
        'cloths':cloths,
        'num_of_cloths':len(cloths),
        'tag':'Dresses',
        }
    return render(request, 'app/dresses.html', context)
