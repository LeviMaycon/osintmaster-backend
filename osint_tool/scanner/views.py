import subprocess
import shlex
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScanRequestSerializer

class ScanAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ScanRequestSerializer(data=request.data)
        
        if serializer.is_valid():
            ip = serializer.validated_data['ip']
            options = serializer.validated_data['options']
            
            safe_ip = shlex.quote(ip)
            safe_options = shlex.quote(options)

            try:
                command = f"nmap {safe_options} {safe_ip}"
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                
                result = result.decode('utf-8')
                
                return Response({"result": result}, status=status.HTTP_200_OK)
            
            except subprocess.CalledProcessError as e:
                return Response({"error": e.output.decode('utf-8')}, status=status.HTTP_400_BAD_REQUEST)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
