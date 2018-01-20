import zipfile

def extractFile(zFile,password):
    try:
        zfile.extractall(pwd=bytes(password,encoding="utf8"))
        print('[+]password OK '+password+'\n')
    except Exception as e:
         print("ERROR :"+str(e))

def main():            
       
    zfile=zipfile.ZipFile('/home/admin/emacs_files/logt.zip','r')
    passfile=open('/home/admin/emacs_files/dictionary.txt','r')
    for line in passfile.readlines():
        password=line.strip('\n')
        print("password="+password+" line="+line)
        extractFile(zfile,password)
    
if __name__=='__main__':
    main()
