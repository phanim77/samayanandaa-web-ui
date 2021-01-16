from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feedback
    fields = ('id', 'first_name', 'last_name', 'email_addr', 'feedback_message_content', 'created_time', 'modified_time')