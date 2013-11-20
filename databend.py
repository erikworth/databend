import os
from random import *
import string
 
 
def data_bend(input_file):
    # Open file in binary mode
    f = open(input_file, "rb")
    data = f.read()
    f.close()
 


    

    for x in range(50):
        #preserve header data
        header = data[:500]
        core = data[500:]
        randstring = ''
        
        #write random strings a random number of times into image data
        for y in range(randint(1,5)):    
            for z in range(randint(1,80)):
                randstring += choice(string.letters + string.digits)

            corelist = list(core)
            corelist.insert(randint(0, len(core) - 1), randstring)
            core = ''.join(corelist)
        
 
        
 
        f = open('%s'%(x)+input_file, "wb")
        f.write(header + core)
        f.close()
