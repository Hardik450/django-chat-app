# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .mongodb import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

collection = messages
#  @Hello123 is a pass
# hardikjain is an user.

# @Hola123 Hello
def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    messages = list(collection.find({"room": "globalroom"}).sort("timestamp", 1))
    return render(request, 'chat.html', {"messages": messages})