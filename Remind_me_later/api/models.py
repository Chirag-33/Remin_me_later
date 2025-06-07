from django.db import models

# Create your models here.
class Reminder(models.Model):
    REMINDER_CHOICES = [
        ('email','Email'),
        ('sms','SMS')
    ]
    
    message = models.TextField()
    remind_at = models.DateTimeField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reminder_type.upper()} reminder at {self.remind_at}"