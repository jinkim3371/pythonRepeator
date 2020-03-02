import os
import time
import shutil
import datetime

### Parameters :
verbose = True
delay = 3600             #dealy for each iteration in seconds.
python_Script = 'NAME OF YOUR SCRIPT'   # ex.'python torrent_web_scraper.py'

### Parameters for filemover :
source = 'PATH OF ORIGINAL FOLDER'
dst = 'PATH TO MOVE THE FILES'
days = 3                 #Files older day N days will be removed.


def timeStamp(verbose=True):
    if verbose:
        dateTimeObj = datetime.datetime.now()
        print ("             Time stamp : ", dateTimeObj.strftime("%Y-%m-%d %H:%M:%S"))

def fileMover():
    files = os.listdir(source)
    num_files = len(files)

    if num_files > 0 :
        print ("\n Start moving files from folder ", source )
        for f in files:
            print("   --- moving", f," file to ", dst)
            shutil.move(os.path.join(source, f), os.path.join(dst, f))
        print ("   ---  %d files were moved to the destination folder.\n " %num_files)


def fileRemover(d=3, verbose = False) :
    now = time.time()
    for f in os.listdir(dst):
        mtime = os.stat(os.path.join(dst,f)).st_mtime
        timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
        timestamp_str_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M')

        if verbose:
            print(f)
            print ("                - Date motified        ", timestamp_str)
            print ("                - Reference time       ", timestamp_str_now)
            print ()

        if os.stat(os.path.join(dst, f)).st_mtime < now - d * 86400:
            print ("======================================================== deleting file : ", f)
            os.remove(os.path.join(dst, f))




#__main__
i = 0
while True:
    timeStamp(verbose=True)
    print ("Iteration :: ",i)
    os.system(python_Script)
    fileRemover(d = days, verbose = False)                 #Function to remove files in a folder. Comment if not needed.
    print("Falling sleep for ", delay, " seconds.       ", )

    timeStamp()
    print()

    time.sleep(delay)
    fileMover()                                            #Function to move files from one folder to anoter. Comment if not needed.
    i+=1

