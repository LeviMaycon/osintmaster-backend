from django.shortcuts import render
from django.http import HttpResponse
from .forms import ScanForm
import subprocess

def home(request):
    return render(request, 'core/home.html')

def scan(request):
    form = ScanForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ip = form.cleaned_data['ip']
        options = form.cleaned_data['options']
        try:
            result = subprocess.check_output(['nmap', options, ip], stderr=subprocess.STDOUT)
            result = result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            result = f"Erro: {e.output.decode('utf-8')}"

        return render(request, 'core/scan_result.html', {'result': result, 'ip': ip})

    return render(request, 'core/scan.html', {'form': form})
