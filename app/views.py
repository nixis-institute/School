from django.shortcuts import render,HttpResponse
import csv

# Create your views here.
def home(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get("DOB")
        w = open("f.csv","w")
        w = csv.writer(w)        
        w.writerow([fname,lname,dob])
        return HttpResponse("Success!")
        #return HttpResponse(abc)
    else:    
        return render(request,"index.html")

def wel(request):
    return render(request,"w.html")