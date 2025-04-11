from django.shortcuts import render
from .models import Perfume

def perfume_list(request):
    perfumes = Perfume.objects.all()[:15]
    return render(request, 'shop/perfume_list.html', {'perfumes': perfumes, 'request': request})


def shop(request):
    all_perfumes=Perfume.objects.all()
    return render(request, 'shop/shop.html', {'all_perfumes': all_perfumes, 'request': request})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')