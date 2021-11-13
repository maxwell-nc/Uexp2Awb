# -*- coding: utf-8 -*-

import os
import mmap

# use buffer copy
def copypart(src,dest,start,length,bufsize=1024*1024):
    with open(src,'rb') as f1:
        f1.seek(start)
        with open(dest,'wb') as f2:
            while length:
                chunk = min(bufsize,length)
                data = f1.read(chunk)
                f2.write(data)
                length -= chunk


# find mark and split
def splitUexp(root,file):
    inPath=os.path.join(root,file)
    with open(inPath, 'rb') as f:
        print(f.name);
        s = f.read()
        # AFS2
        afs2pos = s.find(b'\x41\x46\x53\x32')
        
        if afs2pos == -1:
            print("not awb find!")
            return
        
        # @UTF
        endPos = s.find(b'\x40\x55\x54\x46',afs2pos)

        print("find:{0}".format(afs2pos))
        print("end:{0}".format(endPos)) 
    outPath=os.path.join(root,file+".awb")
    copypart(inPath,outPath,afs2pos,endPos-afs2pos)
            
    

# find all uexp under current folder
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".uexp"):
            splitUexp(root,file)
print("finish")
