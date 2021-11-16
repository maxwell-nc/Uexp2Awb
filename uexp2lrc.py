# -*- coding: utf-8 -*-

import os
import json

def second2time(seconds):
    m, s = divmod(seconds, 60)
    return "[%02d:%05.2f]" % (m, s)


def loadJson(root,file):
    lrcList = ['[offset:0]']
    inPath=os.path.join(root,file)
    with open(inPath,'r',encoding='utf-8')as fp:
        j_data = json.load(fp)
        for index in j_data[0]['Rows']:
            lryic = j_data[0]['Rows'][index]['Lyric']
            begin = j_data[0]['Rows'][index]['DisplayTime']
            end = j_data[0]['Rows'][index]['HiddenTime']
            lrcList.append(second2time(begin)+lryic)
            lrcList.append(second2time(end))
    if len(lrcList) > 0:
        outPath=os.path.join(root,file+".lrc")
        with open(outPath,'w',encoding='utf-8')as fp:
            for line in lrcList:
                fp.write(line+'\n')

# load all txt
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".txt"):
             try:
                loadJson(root,file)
                print(file+" success")
             except Exception as e:
                print(file+" failed: {0}".format(e))
                
print("finish")
