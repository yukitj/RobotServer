from django.shortcuts import render
from django.http import HttpResponse

import socket, json

def get_robots_info():
    HOST = '192.168.2.100'    # The remote host
    PORT = 9999              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'get_robots_info')
        data = s.recv(4096)
        return data

# Create your views here.

def index2(request):
    return HttpResponse(get_robots_info())

def index(request):
    info_dict = json.loads(get_robots_info())
    context = {'info_dict': info_dict}
    return render(request, 'robotinfo/index.html', context)

