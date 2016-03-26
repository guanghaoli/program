# Print all the file in the current directory path
# 2015/11/20 0:44
# @Author Li Guanghao
# University of Chinese Academy of Science
import os
#from os import path
file_path1=os.getcwd()
#help(os.path)
#print dir(os.path)
#print dir(os)
#print os.path.dirname(file_path)
def print_dir(file_path):
    for file_within in os.listdir(file_path):
        ## os.listdir list all the file in the path
        if os.path.isdir(os.path.join(file_path,file_within))==0:
            print "This is a file: ", os.path.join(file_path,file_within)
        else:
            file_within = os.path.join(file_path,file_within)
            print "This is a directory:",file_within
            print_dir(file_within)
            # os.path.join(path,file) Get the absolute path of the file
           
        
print_dir(file_path1)
