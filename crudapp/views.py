from django.http import HttpResponse
from django.http import JsonResponse
from .models import employee
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return HttpResponse ("hello all")

@csrf_exempt
def addemployee(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            name=data.get('name')
            dob=data.get('dob')
            department=data.get('department')
            address=data.get('address')
            if not all ([name,dob,department,address]):
                return JsonResponse({'error':'missing required fields'},status=400,)
            Employee = employee.objects.create(name=name,dob=dob,department=department,address=address)
            return JsonResponse({'message':'employee details created successfully',
                                 'employee id':Employee.id,
                                 'status':'201'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON','status_code':'400'}, status=400)
    return JsonResponse("error:only POST method is allowed")

@csrf_exempt
def employeeget(request,pk=None):
    if request.method=='GET':
        if pk:
            try:
                Employee = employee.objects.get(pk=pk)
                return JsonResponse({
                    'name':Employee.name,
                    'dob':Employee.dob,
                    'department':Employee.department,
                    'address':Employee.address})
            except employee.DoesNotExist:
                return JsonResponse({'error':'employee does not exist'})
        else:
            Employee=list(employee.objects.all().values())
            return JsonResponse(Employee, safe=False)
        
@csrf_exempt
def employeeupdates(request,pk=None):
    if request.method=='PATCH':
        try:
            Employee=employee.objects.get(pk=pk)
            data=json.loads(request.body)
            if 'name' in data: Employee.name = data['name']
            if 'dob' in data:Employee.dob=data['dob']
            if 'department' in data:Employee.department=data["department"]
            if 'address'in data:Employee.address=data['address']
            Employee.save()
            return JsonResponse({'message':f'employee details for id: {pk}  updated successfully'})
        except employee.DoesNotExist:
            return JsonResponse({'error':'this employee not found'},status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid json'},ststus=400)
        
    elif request.method=='PUT':
        try:
            Employee=employee.objects.get(pk=pk)
            data=json.loads(request.body)
            Employee.name=data.get('name',Employee.name)
            Employee.dob=data.get('dob',Employee.dob)
            Employee.department=data.get('department',Employee.department)
            Employee.address=data.get('address',Employee.address)
            Employee.save()
            return JsonResponse({'message':f'employee details for id: {pk}  changed successfully'})
        except employee.DoesNotExist:
            return JsonResponse({'error':'this employee not found'},status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid json'},ststus=400)
        
@csrf_exempt    
def employeedelete(request,pk=None):
    if request.method=='DELETE':
        try:
            Employee=employee.objects.get(pk=pk)
            data=json.loads(request.body)
            Employee.delete()
            return JsonResponse({'message':f'employee details for id: {pk}  deleted successfully'},status=201)
        except employee.DoesNotExist:
            return JsonResponse({'error':'this employee not found'},status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error':'invalid json'},ststus=400)
        
        
        
                
            
            
        
            
                       
        
            
        
        
            
            
            
            
    



            
            
            
            
            
            
         
            


    