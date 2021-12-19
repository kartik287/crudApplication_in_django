from django.shortcuts import render
from .forms import MessageForm
from django.http.response import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'PcNation/home.html')

def services_view(request):
    return render(request, 'PcNation/services.html')

def portfolio_view(request):
    return render(request, 'PcNation/portfolio.html')

def about_view(request):
    return render(request, 'PcNation/about.html')

def team_view(request):
    return render(request, 'PcNation/team.html')

def contact_view(request):
    if request.method=='GET':
        frm_unbound=MessageForm()
        d1={'form':frm_unbound}
        return render(request, 'PcNation/contact.html', context=d1)

    elif request.method=='POST':
        frm_bound=MessageForm(request.POST, files=request.FILES)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("<h2>THANKS FOR YOUR FEEDBACK.</h2> <a href='http://127.0.0.1:8000/pcn/contact/'>Back</a>")
        else:
            d1={'form':frm_bound}
            return render(request, 'PcNation/contact.html', context=d1)