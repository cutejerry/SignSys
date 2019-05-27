from django.shortcuts import render

from django.http import HttpResponse, FileResponse
from django.utils.http import urlquote
import os

# Create your views here.
def download(request):
    file_name = request.GET.get('file', '')

    try:
        basedir = os.path.dirname(os.path.abspath(__name__))
        full_path = basedir + '/Documents/' + file_name
        print(full_path)
        file = open(full_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        # response['Content-Disposition'] = 'attachment;filename=' + file_name#.encode('utf-8')
        response['Content-Disposition'] = 'attachment;filename="%s"'%(urlquote(file_name))
        return response
    except Exception:
        return HttpResponse("File not found.", status=404)