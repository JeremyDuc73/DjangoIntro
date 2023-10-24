from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

# Create your views here.


def index(request):

    return render(request, 'website/home.html')


def bidule(request):
    return render(request, 'website/bidule.html', {
        "bidule": "un nouveau message"
    })


def all_messages(request):
    form = MessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("all_messages")
    messages = Message.objects.all()

    return render(request, 'website/all.html', {"form": form, "messages": messages})


def show_message(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'website/show.html', {"message": message})


def delete_message(request, id):
    Message.objects.filter(id=id).delete()

    return redirect('all_messages')


