import imp
from employeeapi.viewsets import EmployeeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employee',EmployeeViewSet)


#localhost:p/api/amployee/5
#GET, POST, UPDATE, DELETE
# list, retrive

