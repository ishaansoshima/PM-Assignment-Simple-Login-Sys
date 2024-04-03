from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    return render(request,"index.html")

'''def contact(request):
    info={}
    try:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST.get('email')
            info={'name':name,'email':email}
    except:
        pass
    return render(request,"contact.html",info)'''


'''def contact(request):   using get method
    info={}
    try:
        if request.method=="GET":
            name=request.GET['name']
            email=request.GET.get('email')
            info={'name':name,'email':email}
    except:
        pass
    return render(request,"contact.html",info)'''
