from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    #Note the key boldmessage mastches to {{ boldmesage }} in the template!
    # From part 3 return HttpResponse("Rango says hey there partner! <a href= '/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page. <a href= '/rango/'>Index</a>")
    return render(request, 'rango/about.html')
