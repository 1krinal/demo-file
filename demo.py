
print("------ALL INSTALLED SOFTWERE'S LIST------")

import subprocess 


list_data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
data = str(list_data) 
try: 
    
    for i in range(len(data)): 
        print(data.split("\\r\\r\\n")[1:][i]) 
  
except IndexError as e: 
    print("all dta list....")

print("------INTERNET SPEED------")

import speedtest
import math
def convert_mb(size_of_byte):
    i=int(math.floor(math.log(size_of_byte,1024)))
    power=math.pow(1024,i)
    s=round(size_of_byte/power,3)
    return f"{s}"

s=speedtest.Speedtest()
download_speed=s.download()
upload_speed=s.upload()
print("for the download speed:",convert_mb(download_speed))
print("for the uplode speed:",convert_mb(upload_speed))


print("------CSREEN RESOLVUTION------")


import ctypes

def screen_resolution():
    s_r = ctypes.windll.user32
    width = s_r.GetSystemMetrics(0)
    height = s_r.GetSystemMetrics(1)

    return width, height

print(screen_resolution())


print("------CPU MODEL------")

import platform

def cpu_model():
    return platform.processor()

print(cpu_model())


print("------NUMBER OF CORE AND THREADS OF CPU------")

import psutil

def core_threads():
    core = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)

    return core, threads

core, threads = core_threads()
print(f"Number of Cores: {core}")
print(f"Number of Threads: {threads}")


print("------GPU MODEL(IF EXIST)------")

import GPUtil

g = GPUtil.getGPUs()

if len(g) > 0:
    gpu = g[5]
    gpu_model = gpu.name
    print(f"GPU Model: {gpu_model}")
else:
    print("No GPU available or accessible.")


print("------SCREEN SIZE------")



import tkinter
size = tkinter.Tk()
width = size.winfo_screenwidth()
height = size.winfo_screenheight()
print("width=",width )
print("height=",height)

print("------RAM SIZE------")

import psutil

total_ram_b = psutil.virtual_memory().total
ram_gb = total_ram_b / (1024 ** 3) 
print(f"Total RAM: {ram_gb:.2f} GB")



print("------WIFI/ETHERNET MAC ADDRESS------")



from getmac import get_mac_address

mac_addresses = get_mac_address()

print(f"MAC Address(es): {mac_addresses}")


print("------PUBLIC IP ADDRESS------")

import requests

def ip():
    response = requests.get('https://api.ipify.org')
    return response.text

print("Public IP address: ", ip())


print("------WINDOWS VERSION------")

import platform

def windows_version():
    if platform.system() == 'Windows':
        return platform.release()
    else:
        return 'Not a Windows system'

print(windows_version())