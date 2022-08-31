import time
import os
import subprocess
import sys
import shutil
import ctypes 

from tqdm import tqdm #progressbar
      
print("Simulator Automated Boot and Service Start....")

from urllib import request

# Set stage and create tmp folder ----------------------
subprocess.call("cmd /c mkdir tmp")
# Wait for folder to be built
for i in tqdm (range (101), 
               desc="Loading...", 
               ascii=False, ncols=75):
    time.sleep(0.01)
time.sleep(3)

# Download remote and save locally ----------------------
# Define the remote file to retrieve
remote_url = 'https://www.google.com/robots.txt'
# Define the local filename to save data
local_file = 'tmp/123456.txt'

request.urlretrieve(remote_url, local_file)

# Wait for file to be placed in folder
for i in tqdm (range (101), 
               desc="Staging...", 
               ascii=False, ncols=75):
    time.sleep(0.01)
time.sleep(3)


# Wait for script to run ----------------------
for i in tqdm (range (101), 
               desc="Running...", 
               ascii=False, ncols=75):
    time.sleep(0.01)

# Run Script
#subprocess.call("notepad") # works
#subprocess.call("cmd /c test.vbs")

time.sleep(3) # Sleep for 10 seconds

# Cleanup  ----------------------
for i in tqdm (range (101), 
               desc="Cleanup...", 
               ascii=False, ncols=75):
    time.sleep(0.01)
# Remove Script to protect
os.remove("tmp/123456.txt") #file
shutil.rmtree("tmp")   #folder

# Show completion message
ctypes.windll.user32.MessageBoxW(0, "Boot Process Complete", "SimStart", 1)

