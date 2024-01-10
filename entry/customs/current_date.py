from django.utils import timezone

def current_datatime():
    return timezone.now().strftime('%A, %b %d, %Y')