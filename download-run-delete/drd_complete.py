import time
import os
import subprocess
import sys
import shutil
import ctypes 
from tqdm import tqdm #progressbar
from urllib import request #main

######
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
######

subprocess.call("cmd /c cls")
print("")
print(f"{bcolors.OKCYAN}##############################################{bcolors.ENDC}")   
print("# Simulator Automated Boot and Service Start #")
print(f"{bcolors.OKCYAN}##############################################{bcolors.ENDC}")  
print("")
########################################################
# Set stage and create tmp folder ----------------------
subprocess.call("cmd /c mkdir tmp")
# Wait for folder to be built
for i in tqdm (range (100), 
               desc="Staging...", 
               ascii=False, ncols=75):
    time.sleep(0.01)
time.sleep(1)
#########################################################
# Download remote and save locally ----------------------
# Define the remote file to retrieve
remote_url = 'https://www.google.com/robots.txt'
# Define the local filename to save data
local_file = 'tmp/123456.txt'
# Retreive the file defined above
request.urlretrieve(remote_url, local_file)

# Wait for file to be placed in folder
for i in tqdm (range (100), 
               desc="Loading...", 
               ascii=False, ncols=75):
    time.sleep(0.02)
time.sleep(3)

#########################################################
# Run Script (file) -------------------------------------
#subprocess.call("notepad") # works
#subprocess.call("cmd /c test.vbs")

# Wait for script to run
for i in tqdm (range (100), 
               desc="Running...", 
               ascii=False, ncols=75):
    time.sleep(0.04)

# Cleanup  ----------------------
for i in tqdm (range (100), 
               desc="Cleanup...", 
               ascii=False, ncols=75):
    time.sleep(0.01)
# Remove Script to protect
os.remove("tmp/123456.txt") #file
shutil.rmtree("tmp")   #folder

###########################################################
# Completed -----------------------------------------------
# Show completion message (Windows)
# ctypes.windll.user32.MessageBoxW(0, "Boot Process Complete", "SimStart", 1)
# Show completion message (Console)
print("")
print(f"{bcolors.WARNING}[[[ Completed ]]]{bcolors.ENDC}")
print("")
time.sleep(3) # Sleep for 10 seconds
