from django.shortcuts import render,redirect

from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail # to send emails

# Create your views here.
def contact(request):
    if request.method == 'POST':
       listing_id = request.POST['listing_id']
       listing = request.POST['listing']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       user_id = request.POST['listing_id']
       realtor_email = request.POST['listing_id']

       # check if user has already made an enquiry
       if request.user.is_authenticated:
           print('Hello')
           user_id = request.user.id
           has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id
           )
           if has_contacted:
               print('Hello1')
               messages.error(request,'You have already made an enquiry for this Property')
               return redirect('/listings/'+listing_id)   

       contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

       contact.save()
       
       # Send mail
       send_mail(
           'Property Listing',
           'There has been an inquiry for ' + listing + '.Sign in into admin panel for more info',
           'parthi1996@gmail.com',
           [realtor_email,'parthi3113@gmail.com'],
           fail_silently=False
       )

       messages.success(request,'Your request has been submitted,a realtor will get back to you soon')

       return redirect('/listings/'+listing_id)