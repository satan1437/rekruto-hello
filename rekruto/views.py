from django.http import HttpResponse


def index(request):
	name = request.GET.get("name")
	message = request.GET.get("message")
	if name and message:
		return HttpResponse(f"<h1>Hello {name} {message}</h1>")
	return HttpResponse(f"<h1>:(</h1>")
