from django.contrib import admin
from django.urls import path, include
from tracker.views import *

urlpatterns = [

    path('user/', UserAPIView.as_view(), name='user'),

    # for admin
    path("admin/", admin.site.urls),


    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('employees/<int:pk>/assign/', EmployeeAssignListView.as_view(), name='employee-Assign-list'),

    # Device URLs
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('devices/<int:pk>/assign/', DeviceAssignView.as_view(), name='device-assign'),

    
    # for api authentications
    # path('api/', include('rest_framework.urls')),

]
