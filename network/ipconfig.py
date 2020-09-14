""" 
Python Program to Get IP Address 
Written by S Sandeep Pillai

API used: ipify.org

"""
from socket import gethostname, gethostbyname
from requests import get

def dprint(message, debug=False):     
    ''' Debug Print ''' 
    if debug==True: print(message)

def ip4_Private(debug=False):
    ''' returns host private ip address '''
    hostname = gethostname()    
    IPAddr = gethostbyname(hostname)    
    dprint("Your Computer Name is:" + hostname, debug)    
    dprint("Your Computer IP Address is:" + IPAddr, debug)
    return IPAddr 

def ip4_Public(debug=False):
    ''' returns router's public ip address '''
    ip = get('https://api.ipify.org').text
    dprint('My public IP address is:'+ ip, debug)
    return ip 


if __name__ == "__main__":
    ip4_Private(debug=True)
    ip4_Public(debug=True)