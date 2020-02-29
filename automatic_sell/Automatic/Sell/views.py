from django.shortcuts import render,redirect
from . import models
from .serial_param import crc16Check,DOpenPort
import serial

# Create your views here.
# ser=None

def board(request):
    # global ser
    # if ser is None:
    #     ser=DOpenPort("COM3",38400,8,"N",1)

    messages = models.Message.objects.all()

    return render(request,'board.html',{'messages':messages})

from . import serial_param
def msg(request):
   if request.method == 'POST':
        content = request.POST['content']
        content_msg = models.Message.objects.create(content=content)
        return redirect('/board/')
