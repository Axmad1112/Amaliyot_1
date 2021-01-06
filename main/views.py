from django.shortcuts import render

def index(request):
    if request.method=='POST':
        a=int(request.POST["val_1"])
        b=int(request.POST["val_2"])
        s= a+b
        return render(request, "index.html", {"s":s})
    return render(request, "index.html")