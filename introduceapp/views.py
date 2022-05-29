from django.shortcuts import render

# Create your views here.
def Grid(request):
    return render(request, 'Grid.html')

def department2(request):
    return render(request, 'department2.html')

def table(request):
    return render(request, 'table.html')

def test2(request):
    return render(request, 'test2.html')