from django.shortcuts import render

def nav(request):
    return render(request, 'nav.html')


def main(request):
    return render(request, 'main.html')
