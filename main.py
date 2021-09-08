'''
    Created on :  8 Sept,2021
    Author : Mohammad Rehbar
    Library Needs to Install : None
    Works on Linux/Uix & Not yet tested on Windows.
    Python Version : Python 3.9
    
'''

import os,sys,time,glob,pathlib,tarfile
from datetime import datetime
import shutil

#global variable define
log_name= datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
time_name= datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H.%M.%S')
main_path = os.getcwd()
file_in_folder = 'datain'
file_out_folder = 'dataout'
archive_folder = 'archive'
#methods
def __init__():
    #initilizing the directory
    if not os.path.isdir(file_in_folder):
        os.mkdir(file_in_folder)
    if not os.path.isdir(file_out_folder):
        os.mkdir(file_out_folder)
    if not os.path.isdir(archive_folder):
        os.mkdir(archive_folder)

def __check_folders():
    #inside datain directory
    if not os.path.isdir(file_in_folder):
        w = open(log_name+str('.log'),'a')
        w.write('datain directory not present')
        w.close()
        return False
    if not os.path.isdir(file_out_folder):
        w = open(log_name+str('.log'),'a')
        w.write('dataout directory not present')
        w.close()
        return False
    if not os.path.isdir(archive_folder):
        w = open(log_name+str('.log'),'a')
        w.write('archive directory not present')
        w.close()
        return False
    return True
        
def __read_archive_files():
    w = open(log_name+str('.log'),'a')
    w.write('Data Archiving Started at '+str(time_name)+str('\n'))
    path = os.path.join(main_path,file_in_folder)
    os.chdir(path)
    files = os.listdir(path)
    if files == []:
        return False
    tfile = tarfile.open(os.path.join(path,log_name+str('.gz')),"w")
    for file in files:
        w.write('archiving '+str(file)+'\n')
        tfile.add(file)
        w.write('archived '+str(file)+' successfull\n')
    tfile.close()
    os.chdir('..')
    w.write('Data Archived Successfully\n\n')
    w.close
    return True

def __move_backup_fles():
    w = open(log_name+str('.log'),'a')
    w.write('Moving process initiated \n')
    os.chdir(os.path.join(main_path,file_in_folder))
    os.rename(log_name+str('.gz'),time_name+str('.gz'))
    w.write('Successfully renamed the archived file \n')
    shutil.move(os.path.join(os.getcwd(),time_name+str('.gz')),os.path.join(main_path,archive_folder))
    w.write('Successfully moved the archived file \n')
    destination = os.path.join(main_path,file_out_folder)
    source = os.path.join(main_path,file_in_folder)
    files = os.listdir(source)
    for file in files:
        shutil.move(os.path.join(source,file),destination)
    w.write('Successfully moved the archived file \n')
    

    
    


if __name__=='__main__':
    __init__()
    if not __check_folders():
        sys.exit()
    if not __read_archive_files():
        sys.exit()
    __move_backup_fles()
    
