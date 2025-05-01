from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from AWS Deployed Django App!")
