import os
import psutil
import socket
import multiprocessing

os_info = os.uname()
print("The name of machine is ", os_info[1])
print("The operating system name is ", a[0])
print("The operating system version is ", a[3])
print("The number of cpu's is ", multiprocessing.cpu_count())
print("The amount of memory is ", psutil.virtual_memory())
print("The IP address is ", socket.gethostbyname(socket.gethostname()))
