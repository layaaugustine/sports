from django.shortcuts import render,redirect
from .forms import DataForms
from .models import Datas
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DataForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')

    else:
        form = DataForms()
    context = {
        'form':form
    }

    return render(request,'dashboard/index.html',context)

def prediction(request):
    predicted_sports = Datas.objects.all()
    context = {
        'predicted_sports':predicted_sports
    }
    return render(request,'dashboard/prediction.html',context)