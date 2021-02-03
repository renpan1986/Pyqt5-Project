import os
import os.path

#UI文件所在的路径
dir = './'

#列出目录下的所有UI文件
def listUiFiles():
    list = []
    files = os.listdir(dir)
    for filename in files:
        #print(dir+os.sep+filename)
        #print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    return list
    
    
#把扩展名为.ui的文件改成扩展名为.py的文件
def transPyFile(filename):
    return os.path.splitext(filename)[0] + '.py'
    
#列出目录下的所有UI文件
def listQrcFiles():
    list = []
    files = os.listdir(dir)
    for filename in files:
        #print(dir+os.sep+filename)
        #print(filename)
        if os.path.splitext(filename)[1] == '.qrc':
            list.append(filename)
    return list
    
    
#把扩展名为.ui的文件改成扩展名为.py的文件
def transQrcFile(filename):
    return os.path.splitext(filename)[0] + '_rc.py'
    
#调用系统命令把UI文件转换成Python文件
def runMain():
    list = listUiFiles()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile = pyfile,  uifile = uifile)
        #print(cmd)
        os.system(cmd)
    list = listQrcFiles()
    for qrcfile in list:
        pyfile = transQrcFile(qrcfile)
        cmd = 'pyrcc5 {qrcfile} -o {pyfile} '.format(qrcfile = qrcfile,pyfile = pyfile)
        #print(cmd)
        os.system(cmd)
        
if __name__ == '__main__':
    runMain()
