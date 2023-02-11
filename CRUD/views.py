from django.shortcuts import redirect,render
from APP.models import Employees
def INDEX(request):
    emp=Employees.objects.all()

    context={
        'emp':emp,
    }

    return render(request,'index.html',context)