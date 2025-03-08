from django import forms

class ScanForm(forms.Form):
    ip_address = forms.GenericIPAddressField(label='IP Address', required=True)
    port = forms.IntegerField(label='Port', required=False)
