# appform/views.py
from django.shortcuts import render
from .models import Customer
from .forms import NewSubscriber  # Import the NewSubscriber form

def index(request):
    return render(request, 'index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers': customer_list}
    return render(request, 'customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()

    if request.method == "POST":
        form = NewSubscriber(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return customers(request)  # redirect to the customers view
        else:
            print("Error: Form invalid")
    
    return render(request, 'subscribe.html', {'form': form})
