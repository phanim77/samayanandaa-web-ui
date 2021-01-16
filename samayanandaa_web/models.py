from django.db import models
from django.utils import timezone
# Create your models here.

class NatalHoroscope(models.Model):
    client_id=models.AutoField(primary_key=True)
    first_name=models.CharField('First name', max_length=30)
    middle_name=models.CharField('Middle name', max_length=30, blank=True, null=True)
    last_name=models.CharField('Last name', max_length=30)
    date_of_birth=models.DateField('Date of Birth', null=True)
    time_of_birth_hh=models.CharField('Time of Birth Hour', max_length=2, null=True)
    time_of_birth_mm=models.CharField('Time of Birth Minute', max_length=2, null=True)
    time_of_birth_ss=models.CharField('Time of Birth Second', max_length=2, null=True)
    place_of_birth=models.CharField('Place of Birth', max_length=80)
    current_location=models.CharField('Current Location', max_length=80)
    email_addr=models.EmailField()
    message=models.CharField(max_length=500)
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField(null=True)
    def save(self, *args, **kwargs):
        if not self.client_id:
            self.created_time = timezone.now()
            self.modified_time = timezone.now()
        return super(NatalHoroscope, self).save(*args, **kwargs)
class Feedback(models.Model):
    first_name=models.CharField('First name', max_length=30)
    last_name=models.CharField('Last name', max_length=30)
    email_addr=models.EmailField()
    feedback_message_content=models.CharField(max_length=2000) 
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField(null=True)     
    def save(self, *args, **kwargs):
        self.created_time = timezone.now()
        self.modified_time = timezone.now()
        return super(Feedback, self).save(*args, **kwargs)  
class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    client_id=models.ForeignKey(
        NatalHoroscope, on_delete=models.CASCADE)
    receipt_email=models.EmailField()
    amount=models.FloatField()
    paid_status=models.BooleanField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField(null=True)
    charge_id=models.CharField('Charge ID', max_length=32, null=True)
    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.created_time = timezone.now()
            self.modified_time = timezone.now()
        return super(Payment, self).save(*args, **kwargs)
