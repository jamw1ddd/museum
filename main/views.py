from email import message
from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def contact_view(request):
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or show success message
    return render(request, 'contact.html', {'form': form})

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about1.html')

def membership(request):
    return render(request, 'membership.html')

def gallery(request):
    return render(request, 'gallery.html')