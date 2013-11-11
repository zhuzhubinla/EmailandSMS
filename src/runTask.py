'''
Created on 2013-9-2

@author: bin.zhu
'''

from ThreadTask import threadTask

def main():
    runtask=threadTask()
    runtask.start()

if __name__=="__main__":
    main()
    
    