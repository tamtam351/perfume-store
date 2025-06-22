from django.shortcuts import render
from .models import Perfume

def perfume_list(request):
    # Home: Last 15 perfumes
    perfumes = Perfume.objects.all().order_by('-id')[:15]
    return render(request, 'shop/perfume_list.html', {'perfumes': perfumes, 'request': request})

def shop(request):
    # All perfumes for product page
    all_perfumes = Perfume.objects.all()
    return render(request, 'shop/shop.html', {'all_perfumes': all_perfumes, 'request': request})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')
