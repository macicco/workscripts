# import numpy as np
import glob
import time
import sys
import os

def update_progress(progress):
    """
    Progress Bar to visualize the status of a procedure
    ___
    INPUT:
    progress: percent of the data

    ___
    Example:
    print ""
    print "progress : 0->1"
    for i in range(100):
        time.sleep(0.1)
        update_progress(i/100.0)
    """
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
