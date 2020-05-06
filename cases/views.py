from django.shortcuts import render
import requests

# Create your views here.
def case(request):
    url="https://covid19.mathdro.id/api/countries/{}"
    country=request.POST.get("country")
    print(country)
    #country="India"
    s=requests.get(url.format(country))
    print(s.text)
    r=requests.get(url.format(country)).json()
    weather={

        'country':country,
        'confirmed':r['confirmed']["value"],
        'recovered':r['recovered']['value'],
        'deaths':r['deaths']['value'],

        'last':r['lastUpdate']
        
    }
    context={'weather':weather}
    print(weather)
    return render(request,"index.html",context)
    