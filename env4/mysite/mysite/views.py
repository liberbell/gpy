from django.http import HttpResponse

# 2nd Try
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
