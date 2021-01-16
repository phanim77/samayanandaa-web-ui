from django import forms
from django.forms import ModelForm
from samayanandaa_web.models import NatalHoroscope
from samayanandaa_web.models import Payment
from samayanandaa_web.models import Feedback

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ('first_name', 'last_name', 'email_addr', 'feedback_message_content' )

class NatalHoroscopeForm(ModelForm):
	class Meta:
		model = NatalHoroscope
		fields = ('client_id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'time_of_birth_hh', 'time_of_birth_mm', 'time_of_birth_ss', 'place_of_birth', 'current_location', 'email_addr', 'message' )

class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = ('client_id', 'receipt_email', 'amount', 'paid_status', 'charge_id')
