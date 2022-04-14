#!/usr/bin/env python
import sys
from os import path
import pandas as pd


def main():
    #used to skip program name in argument list
    atProgName = True
    #added output to be printed later
    output = []
    spot = 0
    #go through list of argument file names
    for arg in sys.argv:
        #if argument position isnt program name and path to file exists continue
        if not atProgName and path.exists(arg):
            #read in chunks otherwise could have memory issues
            reader = pd.read_csv(arg,chunksize=1000,sep=',')
            #with open(arg,mode='r') as csvfile:
              #  reader = csv.reader(csvfile)
            for group in reader:
                #uses rfind to find the occurance of last / in path name to extract just filename
                fileName = arg[arg.rfind('/')+1:]
                #add filename column
                group['filename'] = fileName
                #group.append(fileName)
                output.append(group)
        #file is not found so produce error
        elif not atProgName:
            print("Error File does not exist")
        #used after first itteration to allow program to try and access csv files
        atProgName = False
    #used to write header once
    header = True
    #print each line
    for df in output:
        print(df.to_csv(header=header, chunksize=1000, encoding='utf-8-sig',index = False,line_terminator='\r'),end='')
        #after first batch header will be false since it is not needed
        header=False
        

if __name__ == '__main__':
    main()
