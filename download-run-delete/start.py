import time
import os
import subprocess
import sys
import shutil
import ctypes 
from tqdm import tqdm #progressbar
from urllib import request #main

print("")
# Wait for script to run
for i in tqdm (range (200), 
               desc="Safemode...", 
               ascii=True, ncols=75):
    time.sleep(0.01)

# Run Script (file) -------------------------------------
#subprocess.call("notepad") # works
subprocess.call("cmd /c python bin/CITB_run.py")
#subprocess.call("cscript bin/rem.vbs") # works
