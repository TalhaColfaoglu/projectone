from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import About, Education, Experience, Skill, Project, Contact
from .forms import ContactForm

def home(request):
    """Ana sayfa view'ı"""
    about = About.objects.first()
    education = Education.objects.all()[:3]
    experience = Experience.objects.all()[:3]
    skills = Skill.objects.all()
    projects = Project.objects.filter(featured=True)[:6]
    
    context = {
        'about': about,
        'education': education,
        'experience': experience,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """Hakkımda sayfası"""
    about = About.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'about': about,
        'education': education,
        'experience': experience,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Projeler sayfası"""
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    """İletişim sayfası"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)

def contact_ajax(request):
    """AJAX ile iletişim formu"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Mesajınız başarıyla gönderildi!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Geçersiz istek'})
