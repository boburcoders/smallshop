from django.http import HttpResponse
from django.shortcuts import render
from config.models import Product, Category
import requests


def index(request):
    object = Product.objects.all()
    last_five_products = Product.objects.order_by('-created_at')[:5]
    categories = Category.objects.all()
    context = {
        'object': object,
        'last_five_products': last_five_products
    }
    return render(request, 'index.html', context)


def product_detail(request, product_id):
    object = Product.objects.get(id=product_id)
    context = {
        'object': object
    }
    return render(request, 'product.html', context)


def category_detail(request, category_id):
    object = Product.objects.filter(category=category_id)
    context = {
        'objects': object
    }
    return render(request, 'category.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)


def send_message_to_bot(name, email, subject, message):
    token = "<BOT_TOKEN>"
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

    CHAT_ID = '<CHAT_ID>'
    params = {
        'chat_id': CHAT_ID,
        'text': f"New message from: {name}\n Email: {email}:\nSubject: {subject}\nMessage: {message}"
    }

    response = requests.get(telegram_url, params=params)

    # Check the response status
    if response.status_code == 200:
        print("Message sent successfully to the bot.")
    else:
        print("Failed to send message to the bot.")


def contact(request):
    if request.method == 'POST':
        # Extract user information from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_message_to_bot(name, email, subject, message)

    return render(request, 'contact.html')
