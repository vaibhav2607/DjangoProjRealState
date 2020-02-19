from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing1']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an inquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You hav already made an Inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send mail
        send_mail(
            'Property listing Inquiry',
            'There has been an Inquiry for' + listing + '. Sign in into the admin panel for more info.',
            'vaiana1426@gmail.com',
            [realtor_email, 'shanucoc26@gmail.com'],
            fail_silently=False

        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you shortly')
        return redirect('/listings/' +listing_id)
