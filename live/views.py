from django.shortcuts import render
import requests



def world(country):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

    headers = {
        'x-rapidapi-host': "*",
        'x-rapidapi-key': "*"
    }
    querystring = {"country": country}
    worlddata = requests.request("GET", url, headers=headers, params=querystring)
    data1 = [worlddata.json()]
    for ele in data1:
        s = []
        i=0
        for key, value in ele.items():
            i+=1
            if i==4:
                s.append(value)

    return s

def index(request):
    s=world('Global')
    tv=s[0]
    tc=tv['confirmed']
    ta=tv['confirmed'] - tv['recovered']
    tr=tv['recovered']
    td=tv['deaths']
    fv = request.GET.get('country')
    if str(fv) == 'US' or str(fv) == 'us' or str(fv) == 'Us':
        cap = str(fv).upper()
    else:
        cap = str(fv).capitalize()
        cap = "".join(cap.split())
    #print(cap)
    if not fv:
        c0="Please type the country name"
        c1=0
        c2=0
        c3=0
    else:
        s=world(cap)
        bn=s[0]
        c0="Status for "+str(cap)
        c1=bn['confirmed']
        c2=bn['deaths']
        c3=bn['recovered']



    return render(request, 'covid/home.html',{'world':s,'wc1':tc,'wc2':td,'wc3':tr,'wc4':ta,'c1':c1,'c2':c2,'c3':c3,'c0':c0})

