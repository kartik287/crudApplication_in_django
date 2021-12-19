from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from .forms import EmployeeForm
from django.http.response import HttpResponse
from .models import Employee
import traceback

# Create your views here.

def add_employee(request):
    if request.method=='GET':
        frm_unbound=EmployeeForm()
        d1={'form':frm_unbound}
        return render(request, 'crudApplication/register_employee.html', context=d1)

    elif request.method=='POST':
        frm_bound=EmployeeForm(request.POST, files=request.FILES)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("<h2>Employee Add Successfully.</h2> <a href='http://127.0.0.1:8000/crudapp/register/'>Back</a>")
        else:
            d1={'form':frm_bound}
            return render(request, 'crudApplication/register_employee.html', context=d1)

def view_employee(request):
    emp=Employee.objects.all()
    context = {'employees':emp}
    return render(request, 'crudApplication/view_employee.html', context)

def edit_employee(request, id):
    emp=Employee.objects.get(id=id)
    context = {'employee':emp}
    return render(request, 'crudApplication/update_employee.html', context)

def update_employee(request, id):
    employee=Employee.objects.get(id=id)
    # form=EmployeeForm(request.POST, instance=employee)
    # try:
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/crudapp/view')
    # except Exception as e:
    #     trace_back = traceback.format_exc()
    #     message = str(e)+ " " + str(trace_back)
    #     print (message)
    # # else:
    # #     return HttpResponse("Something went wrong. Try again.")
    obj = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crudapp/view')
    context = {'employee':employee}
    return render(request, 'crudApplication/update_employee.html', context)

# def update_employee(request, id):
#     if request.method=='POST':
#         emp=Employee()
#         if Employee.objects.filter(id=id).exists():
#             emp.emp_id=request.POST.get('id')
#             emp.name=request.POST.get('name')
#             emp.address=request.POST.get('address')
#             emp.mobile_no=request.POST.get('mob')
#             emp.email=request.POST.get('email')
#             emp.pic=request.POST.get('img')
#             emp.save()
#             return redirect('/crudapp/view')
#         else:
#             return HttpResponse("Something went wrong. Try again.")

def delete_employee(request, id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/crudapp/view')
            