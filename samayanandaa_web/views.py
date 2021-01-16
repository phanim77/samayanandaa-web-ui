from django.shortcuts import render
from samayanandaa_web.forms import FeedbackForm
from samayanandaa_web.models import Feedback
from samayanandaa_web.forms import NatalHoroscopeForm
from samayanandaa_web.models import NatalHoroscope
from samayanandaa_web.forms import PaymentForm
from samayanandaa_web.models import Payment
from samayanandaa_web.mail import send_mail
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect
from samayanandaa_web import string_formatter_utils
from django.contrib import messages
from samayanandaa_web import utils
from rest_framework import viewsets
from .serializers import FeedbackSerializer

import stripe
# import logging

# Create your views here.
class FeedbackView(viewsets.ModelViewSet):
  serializer_class = FeedbackSerializer
  queryset = Feedback.objects.all()
def feedback_list(request):
    testimonials = Feedback.objects.all()
    print("Myoutput", testimonials)
    return render(request,'#feedback', {'testimonials': testimonials})
def feedback(request): 
    form_class = FeedbackForm
    context = {}
    target_pg = "index.html"
    if request.method == 'POST':
        form = form_class(data=request.POST)             
        if form.is_valid():
            feedback=Feedback()
            print(" feedback form valid")
            feedback.first_name = form.cleaned_data['first_name']
            feedback.last_name = form.cleaned_data['last_name']
            feedback.feedback_message_content = form.cleaned_data['feedback_message_content']
            feedback.email_addr = form.cleaned_data['email_addr']            
            feedback.save()
        else:
            print("form invalid")
            print(form.errors)  
            context['first_name'] = request.POST['first_name']
            context['last_name'] = request.POST['last_name']  
            context['feedback_message_content'] = request.POST['feedback_message_content']
            context['email_addr'] = request.POST['email_addr']
            context['errors'] = form.errors
            for error in form.errors:
                if error == "first_name":
                    context['first_name_missing'] = "true"
                if error == "last_name":
                    context['last_name_missing'] = "true"
                if error == "email_addr":
                    context['email_missing'] = "true"
                if error == "feedback_message_content":
                    context['feedback_message_content'] = "true"   
    else:
        form = form_class()
    testimonials = Feedback.objects.all()
    print("Myoutput", testimonials)
    return render(request,'index.html', {'testimonials': testimonials})
def contact_us(request): 
    return render(request, "#contact_us")
def index(request): 
    form_class = NatalHoroscopeForm
    context = {}
    target_pg = "index.html"
    if request.method == 'POST':
        form = form_class(data=request.POST)             
        if form.is_valid():
            print(" natal horoscope form valid")
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            time_of_birth_hh = form.cleaned_data['time_of_birth_hh']
            time_of_birth_mm = form.cleaned_data['time_of_birth_mm']
            time_of_birth_ss = form.cleaned_data['time_of_birth_ss']
            time_of_birth = time_of_birth_hh + ":" + time_of_birth_mm + ":" + time_of_birth_ss
            place_of_birth = form.cleaned_data['place_of_birth']
            current_location = form.cleaned_data['current_location']
            message = form.cleaned_data['message']
            reply_to = form.cleaned_data['email_addr']
            subject = string_formatter_utils.construct_subject("Natal Horoscope request: " + last_name)
            body = string_formatter_utils.construct_body(first_name, last_name, date_of_birth, time_of_birth, place_of_birth, current_location, message)
            send_mail(reply_to, subject, body)
            newHoroscopeRequest = form.save()
            context['charge_id'] = newHoroscopeRequest.created_time
            context['amount'] = "51.00"
            request.session['charge_id'] = "tmp"
            request.session['client_id'] = newHoroscopeRequest.pk
            return HttpResponseRedirect("#payment")
        else:
            print("form invalid")
            print(form.errors)            
            context['first_name'] = request.POST['first_name']
            context['middle_name'] = request.POST['middle_name']
            context['last_name'] = request.POST['last_name']
            context['date_of_birth'] = request.POST['date_of_birth']
            context['time_of_birth_hh'] = request.POST['time_of_birth_hh']
            context['time_of_birth_mm'] = request.POST['time_of_birth_mm']
            context['time_of_birth_ss'] = request.POST['time_of_birth_ss']
            context['place_of_birth'] = request.POST['place_of_birth']
            context['current_location'] = request.POST['current_location']
            context['message'] = request.POST['message']
            context['email_addr'] = request.POST['email_addr']
            context['errors'] = form.errors
            for error in form.errors:
                if error == "first_name":
                    context['first_name_missing'] = "true"
                if error == "last_name":
                    context['last_name_missing'] = "true"
                if error == "date_of_birth":
                    context['dob_missing'] = "true"
                if error == "time_of_birth":
                    context['tob_missing'] = "true"
                if error == "place_of_birth":
                    context['pob_missing'] = "true"
                if error == "current_location":
                    context['current_location_missing'] = "true"
                if error == "email_addr":
                    context['email_missing'] = "true"
                if error == "message":
                    context['message_missing'] = "true"
            return render(request, "index.html", context)
    else:
        form = form_class()
    testimonials = Feedback.objects.all()
    print("Myoutput", testimonials)
    context['testimonials'] = testimonials
    return render(request, target_pg, context)

def payment(request):
    print ("payment from views.py")
    form_class = PaymentForm
    context = {}
    if request.method == 'POST':
        print ("request method is post")
        form = form_class(data=request.POST)     
        if form.is_valid():   
            print(" payment form valid")
            client_id = form.cleaned_data['client_id']
            token = request.POST.get('stripeToken')            
            receipt_email = form.cleaned_data[('receipt_email')]
            
            amount = form.cleaned_data.get('amount')
            amount = int(amount)
            amount = amount * 100
            
            charge_id = form.cleaned_data['charge_id']
            print("Amount: " + str(amount))
            stripe.api_key = utils.get_secret()['Prod/Samayanandaa/Stripe/Secret']
            print("api key:" + stripe.api_key)
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Real charge',
                source=token,
            )
            form.charge_id = charge.id
            form.client_id = client_id            
            form.receipt_email = receipt_email
            newPayment = form.save()
            print ("Payment id: " + str(newPayment.pk))
            if charge.paid:
                print ("charge paid: ")
                newPayment.paid_status = True
                request.session['charge_id'] = charge.id
                request.session['paid_status'] = 'Success'
                request.session['receipt_email'] = receipt_email
                return HttpResponseRedirect("#natal_horoscope_confirm")
            else:
                print("Payment failed")
                return HttpResponseRedirect("#payment")
        else:
            print("form invalid")
            print(form.errors)
            context['errors'] = form.errors
            return HttpResponseRedirect("#payment")
    else:
        print ("request method is get")
        return render(request, "index.html", context) 
    return render(request, "index.html", context)   