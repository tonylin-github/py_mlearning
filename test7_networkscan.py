
import socket
import os
import time

segment="192.168.1.96/27"
scan_port=(21,22,3389)
seg_list=segment.split('/')
seg_tuple=seg_list[0].split('.')
copy_tuple=seg_tuple[:]
netmask=int(seg_list[1],10)
seg_combine='.'.join(copy_tuple)


if (netmask > 32 or netmask < 0):
    print("illegal segement") 
    os.exit() # end of the program

    
count=2**(32-netmask)
print("count =%d"%(count))

i=0
target=0
while(i<count):
    print(i)
    copy_tuple[3]=str(int(seg_tuple[3],10)+i)
    seg_combine='.'.join(copy_tuple)
    print(seg_combine)
    socket.setdefaulttimeout(0.5)
    s=socket.socket()
    try:
        s.connect((seg_combine,21))
        ans=s.recv(1024)
        print(ans)
        #s.shutdown(2)
        time.sleep(0.5)
        s.close()
        
    except Exception as e:
        print("#ERROR = "+str(e))
    i=i+1

print("last i=%d"%(i))
#print(seg_combine)
