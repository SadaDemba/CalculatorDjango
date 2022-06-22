from django.shortcuts import render
from Calculator.models import Operation
# Create your views here.
def index(request):
    return render(request, "input.html")


def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    op=Operation(num1,num2)
    op.multiplication()
    return render(request, "result.html", {"result": op.getResult()})


