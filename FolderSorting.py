import os
import shutil
import re
import time

# initialisation
##Add your basefile directory here. It is from here the folders are sorted.

#basefile =r"basefile folder directory"

# reference directory
## Add your trigger value and folder directory here, you can add as many as you like 
### Don't forget to remove the # for the line below.

#subject_d = {"trigger value here": r"folder directory here"}


def parsesub(doumentlist):
    for file in doumentlist:
        os.chdir(basefile)
        subject = re.findall("-(\S*)-", file)
        if len(subject) == 0:
            print("could not decode")
        for sub in subject:
            if sub in subject_d.keys():
                 destination = subject_d[sub]
                 shutil.move(file, destination)


while True:
    filenamelist = os.listdir(basefile)
    no_of_files = len(filenamelist)
    time.sleep(10)
    print("___")

    oldnumber = no_of_files
    no_of_files = len(os.listdir(basefile))

    if no_of_files != oldnumber:
        print("i am doing something")
        print(filenamelist)
        parsesub(filenamelist)
