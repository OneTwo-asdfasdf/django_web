from django.shortcuts import render
from .models import Anounce
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Contact
from django.utils import timezone
# Create your views here.



def index(request):
	anounce = Anounce.objects.filter(published__lte=timezone.now()).order_by('published')
	return render(request, 'index.html', {'anounce' : anounce})

def contact(request):
	return render(request, 'contact.html', {})

@csrf_exempt
def contact_check(request):
	if ('name' not in request.POST and 'email' not in request.POST and 'subject' not in request.POST and 'message' not in request.POST):
		return JsonResponse({"status": "fail-post"})
	else:
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		if(len(name) == 0 or len(email) == 0 or len(subject) == 0 or len(message) == 0):
			return JsonResponse({"status": "fail-len"})
		else:
			created = timezone.now()
			Contact.objects.create(name=name, email=email, subject=subject, message=message,created=created)
			return JsonResponse({"status": "success"})
