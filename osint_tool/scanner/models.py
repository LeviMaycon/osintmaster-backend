from django.db import models

# Create your models here.
class ScanResult(models.Model):
  ip_address = models.GenericIPAddressField()
  scan_time = models.DateTimeField(auto_now_add=True)
  result = models.TextField()
  
  def __str__(self):
    return f"Scan for {self.ip_address} at {self.scan_time}"