from django.shortcuts import render
from .models import FakeUserAgent

def user_agent(request):
    data = FakeUserAgent.objects.all()

    return render(request, 'fake_user_agent/user_agent.html', {'data':data})



