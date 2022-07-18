from django.shortcuts import render


def shorter(request):
    return render(request, 'shorter/shorter.html')
