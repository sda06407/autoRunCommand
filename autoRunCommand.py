#!/usr/bin/env python

import os, sys

allTarget = sys.argv[2]
targetList = open(allTarget, "r")
resultPath = sys.argv[3]
Command = sys.argv[1]

if not os.path.isdir(sys.argv[3]):
    os.mkdir(sys.argv[3])

for oneSite in targetList.readlines():
    scanCommand = Command + oneSite[:-1]
    scanResult = os.popen("%s" %scanCommand).read()
    resultName = oneSite.replace("/","_").replace(":","").replace("\n","").replace("\r", "") + ".txt"
    makeResult = open(os.path.abspath(resultPath) + "//" + resultName, "w")
    makeResult.write(scanResult)
    makeResult.close()
