# Decompiler binary IPl files by Roger571 04/02/18

import os
from iplBinary import *

for i in os.listdir("compile"): 
    ipl = iplBinary("compile/" + i)
    if ipl != 0: 
        ipl.Process()
        ipl.writeDecompile("decompile/" + i)