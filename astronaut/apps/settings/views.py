from django.shortcuts import render
from .forms import StudentRegistration
from .models import Post
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['title']
            em = fm.cleaned_data['content']
            reg = Post(title=nm, content=em)
            reg.save()

    else:
        fm = StudentRegistration()
    return render(request,'dashboard/pages/websettings.html',{'form':fm})