from django.shortcuts import render,redirect, get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm
# Create your views here.


# --- Patient Views ---
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient_instance = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient_instance)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient_instance)
    return render(request, 'hospital/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient_instance = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient_instance.delete()
        return redirect('patient_list')
    return render(request, 'hospital/patient_confirm_delete.html', {'patient': patient_instance})

# --- Doctor Views ---
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospital/doctor_form.html', {'form': form})

def doctor_update(request, pk):
    doctor_instance = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor_instance)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor_instance)
    return render(request, 'hospital/doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor_instance = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor_instance.delete()
        return redirect('doctor_list')
    return render(request, 'hospital/doctor_confirm_delete.html', {'doctor': doctor_instance})

# --- Appointment Views ---
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/appointment_form.html', {'form': form})

def appointment_update(request, pk):
    appointment_instance = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment_instance)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment_instance)
    return render(request, 'hospital/appointment_form.html', {'form': form})

def appointment_delete(request, pk):
    appointment_instance = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment_instance.delete()
        return redirect('appointment_list')
    return render(request, 'hospital/appointment_confirm_delete.html', {'appointment': appointment_instance})
