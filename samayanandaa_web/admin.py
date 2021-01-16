from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NatalHoroscope
from .models import Payment
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	list_display = ('first_name', 'last_name', 'email_addr', 'feedback_message_content', 'created_time', 'modified_time')	
admin.site.register(Feedback, FeedbackAdmin)

class NatalHoroscopeAdmin(admin.ModelAdmin):
	model = NatalHoroscope
	list_display = ('client_id', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'time_of_birth_hh', 'time_of_birth_mm', 'time_of_birth_ss', 'place_of_birth', 'current_location', 'email_addr', 'message', 'created_time', 'modified_time')	
admin.site.register(NatalHoroscope, NatalHoroscopeAdmin)

class PaymentAdmin(admin.ModelAdmin):
	model = Payment
	list_display = ('client_id', 'receipt_email', 'amount', 'paid_status', 'created_time', 'modified_time', 'charge_id')
admin.site.register(Payment, PaymentAdmin)