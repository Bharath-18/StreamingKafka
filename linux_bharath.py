import subprocess 
import os 
import pdb
from datetime import date
from datetime import datetime

# a function to list the files in 
# the current directory and  
# parse the output. 


# run('ls -la', 'wc -l')
def list_command(args = 'wc'): 
    # the ls command 
    cmd = 'ls'
    # using the Popen function to execute the 
    # command and store the result in temp. 
    # it returns a tuple that contains the  
    # data and the error if any. 
    temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE) 
    # we use the communicate function 
    # to fetch the output 
    output = str(temp.communicate())   
    # splitting the output so that 
    # we can parse them line by line 
    output = output.split("\n")  
    output = output[0].split('\\') 
    # a variable to store the output 
    res = [] 
    # iterate through the output 
    # line by line 
    for line in output:  
        res.append(line)
    no_of_files = len(res)-1
    return no_of_files
# parse the output of the ls  
# command and fetch the permissions 
# of the files and store them in  
# a text file . 
def get_permissions(): 
    # get the output of the  
    # list command 
    no_of_files = list_command('/home/arima/Desktop/vinod_reddy')
    output = ''
    print(no_of_files)
    

    if no_of_files>3:
        output = "Fail"
    elif no_of_files<3 and no_of_files>0:
        output ="success"
    elif no_of_files == 0:
        output = "No records found"

    os.chdir('outputs') 
  
    # open the output file 
    out = open('permissions.txt', 'a+') 
  
    out.write('{0}:{1}\n\n'.format(datetime.now(),output)) 
  
    # write to the output file  
  
    os.chdir('..') 
  
if __name__ == '__main__': 
    get_permissions() 
