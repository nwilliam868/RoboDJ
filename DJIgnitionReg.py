#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

contentbeats = []
contentdrones = []
contentpepper = []
contentbass = []
contentorg = []
contentsax = []
contentgit = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file


        if  filepath.endswith(".wav") and (("Hop" in str(filepath)) or  ("Dub" in str(filepath))  and "Drums" in str(filepath)):
            contentbeats.append(filepath)

        if  filepath.endswith(".wav") and (("Reggae" in str(filepath)) or  ("Dub" in str(filepath))  and "Pads" in str(filepath)):
            contentdrones.append(filepath)

        if  filepath.endswith(".wav")  and (("Reggae" in str(filepath)) or  ("Dub" in str(filepath))  and "Bass" in str(filepath)) :
            contentbass.append(filepath)

        if  filepath.endswith(".wav") and (("Reggae" in str(filepath)) or  ("Dub" in str(filepath))  and "Keys" in str(filepath)) :
            contentorg.append(filepath)

        if  filepath.endswith(".wav") and (("Reggae" in str(filepath)) or  ("Dub" in str(filepath))  and "Brass" in str(filepath)) :
            contentsax.append(filepath)

        if  filepath.endswith(".wav") and (("Reggae" in str(filepath)) or  ("Dub" in str(filepath)) and "Synth" in str(filepath)) :
            contentgit.append(filepath)

        if  filepath.endswith(".wav") and (("Pad" not in str(filepath)) and ("Drone" not in str(filepath)) and ("Beat" not in str(filepath)) and ("Drum" not in str(filepath))and ("Bass" not in str(filepath)) and ("Tone" not in str(filepath)) and ("OS" not in str(filepath)) and ("Signals" not in str(filepath))  and ("Dialog" not in str(filepath)) and ("Spoken" not in str(filepath)) and ("Guitar" not in str(filepath))) :
            contentpepper.append(filepath)

print("")

print("Gathering Root Sounds.")

x = len(contentbeats)

for ctr in range(80):
    y = random.randrange(x)
    atrack = contentbeats[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundbeat' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbeats[y], outstr)

x = len(contentdrones)

for ctr in range(120):
    y = random.randrange(x)
    atrack = contentdrones[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsounddrone' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentdrones[y], outstr)

x = len(contentpepper)

for ctr in range(150):
    y = random.randrange(x)
    atrack = contentpepper[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundpepper' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentpepper[y], outstr)

x = len(contentbass)

for ctr in range(50):
    y = random.randrange(x)
    atrack = contentbass[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundbass' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbass[y], outstr)

x = len(contentorg)

for ctr in range(100):
    y = random.randrange(x)
    atrack = contentorg[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundgorgan' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentorg[y], outstr)

x = len(contentsax)

for ctr in range(100):
    y = random.randrange(x)
    atrack = contentsax[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundsaxophone' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentsax[y], outstr)

x = len(contentgit)

for ctr in range(100):
    y = random.randrange(x)
    atrack = contentgit[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\RoboDJ\\newsoundguitar' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentgit[y], outstr)

call(["python", "DJProcessorIronMan.py"])

## THE GHOST OF THE SHADOW ##
