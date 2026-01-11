from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_email(booking_id, user_email):
    subject = "Booking Confirmation"
    message = f"Your booking (ID: {booking_id}) has been confirmed. Thank you for choosing us!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
