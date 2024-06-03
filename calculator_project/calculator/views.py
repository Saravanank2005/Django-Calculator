from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'calculator.html')

def calculate(request):# calculator/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')

def add(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        result = num1 + num2
        return render(request, 'calculator/result.html', {'result': result})
    return render(request, 'calculator/add.html')

def subtract(request):
    # Similar implementation to 'add'
    pass

def multiply(request):
    # Similar implementation to 'add'
    pass

def divide(request):
    # Similar implementation to 'add'
    pass

    if request.method == 'POST':
        number_one = request.POST.get('number_one')
        number_two = request.POST.get('number_two')
        operation = request.POST.get('operation')

        if operation == "add":
            result = float(number_one) + float(number_two)
        elif operation == "subtract":
            result = float(number_one) - float(number_two)
        elif operation == "multiply":
            result = float(number_one) * float(number_two)
        elif operation == "divide":
            result = float(number_one) / float(number_two)
        else:
            return HttpResponse("Invalid operation")

        context = {'result': result}
        return render(request, 'calculator.html', context)
    else:
        return HttpResponse("Invalid method")