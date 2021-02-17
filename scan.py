import os
import socket

def ping_host():

    hostname = input("Please input the specific IP Address :")
    result = os.system("ping -c 1 " + str(hostname))

    if result == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is offline!')

def verify_hostname():
    
    

if __name__ == "__main__":
    ping_host()
