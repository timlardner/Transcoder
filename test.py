__author__ = 'Tim'

import os
import pickle

firstrun = False
directory = '/Volumes/Share/HD/Music/Files'

savefile = directory+'/.seen'

if not firstrun:
    seenfolders = pickle.load(open( savefile,'rb'))
else:
    seenfolders = []


folders = os.listdir(directory)

to_transcode = []

for folder in folders:
    if '._' not in folder and folder not in seenfolders:
        to_transcode.append(folder)

# Do transcoding here

print 'Need to transcode ' + str(len(to_transcode)) + ' folders'
for folder in to_transcode:
    # TRANSCODE, then...
    seenfolders.append(folder)
    if not firstrun:
        print folder

pickle.dump(seenfolders, open( savefile,'wb'))