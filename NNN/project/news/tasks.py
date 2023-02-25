from celery import shared_task
from .models import Post
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

@shared_task (post_save, sender=Post)
def post_created(instance, **kwargs):
    if not post_created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новый пост {instance.category}'

    text_content = (
        f'Новость: {instance.title}\n'
        f'Категория: {instance.categoryType}\n\n'
        f'Ссылка на новость: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.title}<br>'
        f'Категория: {instance.categoryType}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()