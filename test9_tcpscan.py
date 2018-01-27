import optparse
import os
import socket

def conn_scan(tgtHost,tgtPort):
    try:
        conn_skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #conn_skt=socket.socket()
#        print('connection ok')
        
        #conn_skt.bind(("192.168.1.110",tgtPort))
        conn_skt.connect((tgtHost,tgtPort))
#        print('bind ok')
        #print('host=%s port=%s'%(tgtHost,tgtPort))
#        conn_skt.send('1')
        results=conn_skt.recv(1024)
#        print('receive ok')
        print('[+]%d/tcp open'%tgtPort)
        print('[+]'+str(results))
        conn_skt.close()
#        print('connection close')
        
    except:
        print('[+]%d/tcp close'%tgtPort)

def port_scan(tgtHost,tgtPorts):
    #tgtIP=socket.gethostbyname(tgtHost)
    #print('ip=%s'%tgtIP)
    '''
    try:

        #tgtIP=socket.gethostbyname(tgtHost)
        #tgtName=socket.gethostbyaddr(tgtIP)
        
        #printf('host=%s ip=%s'%(tgtName[0]))      
    except:
        print("[-]cannot result the '%s': unknow host"%tgtHost)
        return
    try:
        tgtName=socket.gethostbyaddr(tgtIP)
        print('\n[+] scan results for:'+tgtName[0])
    except:
        print("[-]cannot result the '%s': unknow host"%tgtIP)
    '''
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('scanning port'+tgtPort)
        conn_scan(tgtHost,int(tgtPort))

        
        
        
def main():
        usage='usage %prog -H <target host> -p <target port>'
        parser=optparse.OptionParser(usage)
        parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
        parser.add_option('-p',dest='tgtPort',type='string',help='specify target port')
        (options,args)=parser.parse_args()
        
        
        tgtHost=options.tgtHost
        tgtPorts=str(options.tgtPort).split(',')
        #print('host=%s ip=%s'%(tgtHost,tgtPorts))      

        

        
        if(tgtHost==None)|(tgtPorts[0]==None):
            print(parser.usage)
            os.exit()
        port_scan(tgtHost,tgtPorts)
        
if __name__=='__main__':
    main()
