from django.shortcuts import render
from .models import EmployeeModel

# Create your views here.
def showIndex(request):
    return render(request, "index.html")


def registerEmployee(request):
    return render(request, "register.html")


def viewallEmployee(request):
    qs = EmployeeModel.objects.all()
    return render(request, "viewall.html", {"data": qs})


def saveEmployee(request):
    id = request.POST.get("idno")
    na = request.POST.get("name")
    sal = request.POST.get("salary")
    EmployeeModel(salary=sal, id=id, name=na).save()
    return render(request, "index.html", {"message": "Employee Created"})


def updateEmployee(request):
    uid = request.GET.get("update_id")
    #res = EmployeeModel.objects.filter(idno=uid)
    res = EmployeeModel.objects.get(id=uid)
    return render(request, "update.html", {"data": res})


def update_emp(request):
    id = request.POST.get("u_id")
    na = request.POST.get("u_name")
    sal = request.POST.get("u_sal")
    EmployeeModel.objects.filter(id=id).update(name=na, salary=sal)
    return viewallEmployee(request)


def deleteEmp(request):
    did = request.POST.get("del_idno")
    EmployeeModel.objects.filter(id=did).delete()
    return viewallEmployee(request)
