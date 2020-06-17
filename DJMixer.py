#This code imports the necessary modules.

from flask import Flask, render_template
import random
import os
import webbrowser

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = 'noiiugjydyu423irg'

@app.route('/', methods=['POST', 'GET'])
def sessstart():
    return render_template('reanimate.html')

#This code constructs the player page. It chooses an item randomly from a set of lists, and, after processing, opens a player page and cues up the item.

@app.route('/player', methods=['POST', 'GET'])
def make_player():

    outfile = open('AutoPlayListBeats.m3u', "w")

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\RoboDJ\\static'):
        for file in files:
            filepath = subdir + os.sep + file

            if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "beat" in str(filepath):
                cline = str(os.sep + file)
                bline = "\static" + cline
                outfile.write(bline + '\n')

    outfile.close()

    outfile = open('AutoPlayListDrones.m3u', "w")

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\RoboDJ\\static'):
        for file in files:
            filepath = subdir + os.sep + file

            if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "drone" in str(filepath):
                cline = str(os.sep + file)
                bline = "\static" + cline
                outfile.write(bline + '\n')

    outfile.close()


    outfile = open('AutoPlayListPepper.m3u', "w")

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\RoboDJ\\static'):
        for file in files:
            filepath = subdir + os.sep + file

            if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "pepper" in str(filepath):
                cline = str(os.sep + file)
                bline = "\static" + cline
                outfile.write(bline + '\n')

    outfile.close()

    outfile = open('AutoPlayListBass.m3u', "w")

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\thomasoriginalcode\\Git\\RoboDJ\\static'):
        for file in files:
            filepath = subdir + os.sep + file

            if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "bass" in str(filepath):
                cline = str(os.sep + file)
                bline = "\static" + cline
                outfile.write(bline + '\n')

    outfile.close()

    songlength = random.randrange(500, 600)

    infile = open("AutoPlayListBeats.m3u", "r")
   
    contentbeats = []

    plist = infile.readline()
    while plist:
        contentbeats.append(plist)
        plist = infile.readline()
    infile.close()

    infile = open("AutoPlayListDrones.m3u", "r")
   
    contentdrones = []

    plist = infile.readline()
    while plist:
        contentdrones.append(plist)
        plist = infile.readline()
    infile.close()

    infile = open("AutoPlayListPepper.m3u", "r")
   
    contentpepper = []

    plist = infile.readline()
    while plist:
        contentpepper.append(plist)
        plist = infile.readline()
    infile.close()

    infile = open("AutoPlayListBass.m3u", "r")
   
    contentbass = []

    plist = infile.readline()
    while plist:
        contentbass.append(plist)
        plist = infile.readline()
    infile.close()

    atracknum1 = random.randrange(0,len(contentbeats))
    atrack1 = contentbeats[atracknum1]
    atracknum2 = random.randrange(0,len(contentbass))
    atrack2 = contentbass[atracknum2]
    atracknum15 = random.randrange(0,len(contentdrones))
    atrack15 = contentdrones[atracknum15]
    atracknum3 = random.randrange(0,len(contentdrones))
    atrack3 = contentdrones[atracknum3]
    atracknum4 = random.randrange(0,len(contentdrones))
    atrack4 = contentdrones[atracknum4]
    atracknum5 = random.randrange(0,len(contentdrones))
    atrack5 = contentdrones[atracknum5]
    atracknum6 = random.randrange(0,len(contentpepper))
    atrack6 = contentpepper[atracknum6]
    atracknum7 = random.randrange(0,len(contentpepper))
    atrack7 = contentpepper[atracknum7]
    atracknum8 = random.randrange(0,len(contentpepper))
    atrack8 = contentpepper[atracknum8]
    atracknum9 = random.randrange(0,len(contentdrones))
    atrack9 = contentdrones[atracknum9]
    atracknum10 = random.randrange(0,len(contentdrones))
    atrack10 = contentdrones[atracknum10]
    atracknum11 = random.randrange(0,len(contentdrones))
    atrack11 = contentdrones[atracknum11]
    atracknum12 = random.randrange(0,len(contentpepper))
    atrack12 = contentpepper[atracknum12]
    atracknum13 = random.randrange(0,len(contentpepper))
    atrack13 = contentpepper[atracknum13]
    atracknum14 = random.randrange(0,len(contentpepper))
    atrack14 = contentpepper[atracknum14]
    
    

    return render_template('reanimate.html', toplay1 = atrack1, toplay2 = atrack2, toplay3 = atrack3, toplay4 = atrack4, toplay5 = atrack5, toplay6 = atrack6, toplay7 = atrack7, toplay8 = atrack8, toplay9 = atrack9, toplay10 = atrack10, toplay11 = atrack11, toplay12 = atrack12, toplay13 = atrack13, toplay14 = atrack14, toplay15 = atrack15, songlen = songlength )

webbrowser.open('http://localhost:5000')

## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
     app.run()