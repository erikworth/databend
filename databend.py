import os
from random import *
import string
 
 
def data_bend(input_file, output_file):
    # Open file in binary mode
    f = open(input_file, "rb")
    data = f.read()
    f.close()
 
    # preserve header data
    header = data[:500]
    core = data[500:]
    data_size = len(core)

    randstring = ''

    #core = pre + sample + post

    for x in range(randint(1,10)):    
        for y in range(randint(1,300)):
            randstring += choice(string.letters + string.digits)

        corelist = list(core)
        corelist.insert(randint(0, data_size - 1), randstring)
        core = ''.join(corelist)
        
 
        
 
    f = open(output_file, "wb")
    f.write(header + core)
    f.close()
