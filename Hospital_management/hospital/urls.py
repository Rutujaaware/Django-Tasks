from django.urls import path
from . import views

urlpatterns = [
    # Patients
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/update/<int:pk>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:pk>/', views.patient_delete, name='patient_delete'),

    # Doctors
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/update/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),

    # Appointments
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/update/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
]
