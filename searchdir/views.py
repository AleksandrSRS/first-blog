from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormSearche
import os
from django.shortcuts import redirect

def searche_detail(request, y):
    return render(request, 'searchdir/searche_detail.html', {'search': y})

def searche(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name = name.lower()
        listtosearche = ['\\000_GA клиенты', '\\000_Белгород', '\\000_Клиентские договоры MyBOX (ПЕРЕДАНЫ 01.07.2012)',
                         '\\000_Клиентские договоры Крд']

        globalpath = "\\\\192.168.16.3\\Office\\Клиентские договоры"
        G = []
        L = os.listdir(path=globalpath)
        for i in listtosearche:
            K = os.listdir(path=globalpath + i)
            L = L + K
        for x in L:
            y = x.strip()
            y = y.lower()
            y = y.replace(" ", "")
            y = y.replace("_", "")
            y = y.replace("-", "")
            if y.find(name) > -1:
                G.append(x)
        return HttpResponse("<p>" + i + "</p>" for i in G)
        # return redirect('searche_detail', y=y)

    else:
        form_searche = FormSearche()
        return render(request, 'searchdir/index.html', {"form": form_searche})

