import os
import sys,getopt
import pandas as pd
import pyprog
from time import sleep
import decimal

def get_dir_size(dir_name):
    array1 = []
    array = []
    dir_sizes = {}
    for r, d, f in os.walk(dir_name, False):
        

        size = sum(os.path.getsize(os.path.join(r,f)) for f in f+d)
        size += sum(dir_sizes[os.path.join(r,d)] for d in d)
        dir_sizes[r] = size
        size = size/2**20
        rounded = round(size, 2)
        array.append(str(r))
        array1.append(str(decimal.Decimal(rounded).quantize(decimal.Decimal('0.00'))))
    return array,array1
    

def main(argv):
    dirName = ''
    try:
        opts,args = getopt.getopt(argv, "d:",["dirname"])
    except:
        print("-d dirname")
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-d':
            dirName = arg

    filename,filesize = get_dir_size(dirName)
    values = {'Filename':filename,'Filesize in MB':filesize}
    df = pd.DataFrame(values,columns=['Filename','Filesize in MB'])
    df.index = [x for x in range(1, len(df.values)+1)]
    df.index.name = 'SL.NO'
    
    
    df.to_csv('Foldersize.csv')
    print("successfully finished")


if __name__ == '__main__':
    main(sys.argv[1:])
