
import socket
import os

segment="192.168.1.0/24"
scan_port=(21,22,3389)
seg_list=segment.split('/')
seg_tuple=seg_list[0].split('.')
netmask=int(seg_list[1],10)



if (netmask > 32 or netmask < 0):
    print("illegal segement") 
    os.exit() # end of the program

    
count=2**(32-netmask)-2

print(seg_tuple)
