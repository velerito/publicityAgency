from django.shortcuts import render

def news_list(request):
    return render(request, 'publicity_agency/home.html', {})

def order(request):
    return render(request, 'publicity_agency/order.html', {})

def requirements(request):
    return render(request, 'publicity_agency/requirements.html', {})

def contact(request):
    return render(request, 'publicity_agency/contacts.html', {})
