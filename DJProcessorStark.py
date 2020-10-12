#This code imports the necessary modules.

from pydub import AudioSegment
import random
import os
from subprocess import call

contentbeats = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "beat" in str(filepath):
            cline = str(file)
            contentbeats.append(cline)

contentdrones = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "drone" in str(filepath):
            cline = str(file)
            contentdrones.append(cline)

contentpepper = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "pepper" in str(filepath):
            cline = str(file)
            contentpepper.append(cline)

contentbass = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "bass" in str(filepath):
            cline = str(file)
            contentbass.append(cline)

contentorg = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "organ" in str(filepath):
            cline = str(file)
            contentorg.append(cline)

contentsax = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "sax" in str(filepath):
            cline = str(file)
            contentsax.append(cline)

contentgit = []

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\RoboDJ\\'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav") and ("newsample" not in str(filepath)) and "guitar" in str(filepath):
            cline = str(file)
            contentgit.append(cline)

print("Extracting samples. Please wait.")

print("")


for ctr in range(50):

    astr = ("Beat Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentbeats))
    atrack = contentbeats[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    bstr = ("Bass Sample: " + str(ctr + 1))
    print(bstr)
        
    songchb = random.randrange(0,len(contentbass))
    btrack = contentbass[songchb]


    cstr = ("Organ Sample: " + str(ctr + 1))
    print(cstr)
        
    songchc = random.randrange(0,len(contentorg))
    ctrack = contentorg[songchc]        

    try:

        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random.randrange(14,18)
        newAudio = newAudio - newvol
        newAudio = newAudio.fade_in(10)
        newAudio = newAudio.fade_out(10)

        newAudiob = AudioSegment.from_wav(btrack)
        
        newvolb = random.randrange(18,22)
        newAudiob = newAudiob - newvolb
        newAudiob = newAudiob.fade_in(10)
        newAudiob = newAudiob.fade_out(10)

        newAudioc = AudioSegment.from_wav(ctrack)
        
        newvolc = random.randrange(18,22)
        newAudioc = newAudioc - newvolc
        newAudioc = newAudioc.fade_in(10)
        newAudioc = newAudioc.fade_out(10)

        newAudiod = newAudio.overlay(newAudiob)
        print ("overlaying recording")

        newAudioe = newAudiod + newAudiod + newAudiod + newAudiod 

        newAudiof = newAudioe.overlay(newAudioc)

        for cotr in range(7):

            newAudiof = newAudiof + newAudiof

        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsamplebeat" + tracknam + str(ctr) + ".wav"
        newAudiof.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(150):

    astr = ("Drone Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentdrones))
    atrack = contentdrones[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random.randrange(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random.randrange(1000, 2000)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(20,24)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(100)
            newAudio = newAudio.fade_out(100)
            sil1 = random.randrange(2000, 6000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random.randrange(8000, 24000)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(20,24)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(2000, 20000)
            sil2 = random.randrange(3000, 40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random.randrange(20000, 36000)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(20,24)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(3000, 60000)
            sil2 = random.randrange(6000, 40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random.randrange(200, 800)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(20,24)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(10)
            newAudio = newAudio.fade_out(10)
            addAudio = newAudio
            ctr = random.randrange(5,30)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(5000, 60000)
            sil2 = random.randrange(7000, 40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random.randrange(10)
        if dic == 7:
            sil1 = random.randrange(90000)
            sil2 = random.randrange(90000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsampledrone" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(250):

    astr = ("Other Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentpepper))
    atrack = contentpepper[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        solonum = random.randrange(13)
        if solonum < 4:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random.randrange(800, 2400)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(24,30)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(100)
            newAudio = newAudio.fade_out(100)
            sil1 = random.randrange(4000)
            back = AudioSegment.silent(duration = sil1)
            newAudio = newAudio + back
        if solonum > 3 and solonum < 8:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random.randrange(8000, 24000)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(24,30)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(20000)
            sil2 = random.randrange(40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 7 and solonum < 11:
            leng = len(newAudio)
            if leng > 60000:
                samplen = random.randrange(20000, 36000)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(24,30)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(60000)
            sil2 = random.randrange(40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        if solonum > 10:
            leng = len(newAudio)
            if leng > 10000:
                samplen = random.randrange(200, 800)
                sampst = int(leng - samplen)
                t1 = random.randrange(sampst)
                t2 = (t1 + samplen)
                newAudio = newAudio[t1:t2]
            newvol = random.randrange(24,30)
            newAudio = newAudio - newvol
            newAudio = newAudio.fade_in(10)
            newAudio = newAudio.fade_out(10)
            addAudio = newAudio
            ctr = random.randrange(5,30)
            for sam in range(ctr):
                newAudio += addAudio
            newAudio = newAudio.fade_in(3000)
            newAudio = newAudio.fade_out(3000)
            sil1 = random.randrange(60000)
            sil2 = random.randrange(40000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back

        dic = random.randrange(10)
        if dic == 7:
            sil1 = random.randrange(90000)
            sil2 = random.randrange(90000)
            front = AudioSegment.silent(duration = sil1)
            back = AudioSegment.silent(duration = sil2)
            newAudio = front + newAudio + back
        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsamplepepper" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")


for ctr in range(150):

    astr = ("Organ Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentorg))
    atrack = contentorg[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random.randrange(21, 24)
        newAudio = newAudio - newvol
        newAudio = newAudio + newAudio + newAudio + newAudio
        newAudio = newAudio.fade_in(10)
        newAudio = newAudio.fade_out(10)

        sil2 = random.randrange(25000,54000)

        back = AudioSegment.silent(duration = sil2)
        
        newAudio = newAudio + back
        
        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsampleorgan" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(100):

    astr = ("Saxophone Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentsax))
    atrack = contentsax[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random.randrange(27, 29)
        newAudio = newAudio - newvol
        newAudio = newAudio + newAudio + newAudio
        newAudio = newAudio.fade_in(10)
        newAudio = newAudio.fade_out(10)

        sil2 = random.randrange(20000,60000)

        back = AudioSegment.silent(duration = sil2)
        
        newAudio = newAudio + back
        
        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsamplesaxophone" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

for ctr in range(150):

    astr = ("Guitar Sample: " + str(ctr + 1))
    print(astr)
        
    songch = random.randrange(0,len(contentgit))
    atrack = contentgit[songch]
    trackname = atrack[-16:]
    tracknam = ""
    for x in trackname:
        if x.isalnum():
            tracknam += x

    try:
        newAudio = AudioSegment.from_wav(atrack)
        
        newvol = random.randrange(25, 29)
        newAudio = newAudio - newvol
        newAudio = newAudio + newAudio + newAudio
        newAudio = newAudio.fade_in(10)
        newAudio = newAudio.fade_out(10)

        sil2 = random.randrange(22000,48000)

        back = AudioSegment.silent(duration = sil2)
        
        newAudio = newAudio + back
        
        oufil = "C:\\Users\\mysti\\Coding\RoboDJ\\static\\newsampleguitar" + tracknam + str(ctr) + ".wav"
        newAudio.export(oufil, format="wav")
    except:
        print("File unreadable.")

call(["python", "DJMixer4.py"])

## THE GHOST OF THE SHADOW ##
