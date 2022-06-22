from django.shortcuts import render
from Calculator.models import Operation
# Create your views here.
def index(request):
    return render(request, "input.html")

def addition(request):

    op1:str = request.POST['num1']
    op2:str = request.POST['num2']

    op=Operation(op1,op2)
    op.addition()
    return render(request, "result.html", {"result": op.getResult()})


def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    op=Operation(num1,num2)
    op.multiplication()
    return render(request, "result.html", {"result": op.getResult()})


def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    op=Operation(num1,num2)
    op.division()
    return render(request, "result.html", {"result": op.getResult()})