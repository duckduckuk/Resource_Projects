import time
import os
import subprocess
import sys
import shutil

from urllib import request
# Define the remote file to retrieve
remote_url = 'https://www.google.com/robots.txt'
# Create tmp folder
subprocess.call("cmd /c mkdir tmp")
# Wait for folder to be built
time.sleep(3)
# Define the local filename to save data
local_file = 'tmp/123456.txt'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)

# Run Script
#subprocess.call("notepad") # works
#subprocess.call("cmd /c test.vbs")

#wait
time.sleep(10) # Sleep for 10 seconds

# Remove Script to protect
os.remove("tmp/123456.txt") #file
shutil.rmtree("tmp")   #folder
