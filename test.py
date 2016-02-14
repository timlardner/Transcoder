__author__ = 'Tim'

import os
import pickle

def doTranscode(folder):
    fullpath = directory + '/' + folder
    for root, dirs, files in os.walk(fullpath):
        for filename in files:
            if filename.endswith('.flac'):
                to_ffmpeg = os.path.join(root, filename)
                output_name = to_ffmpeg[:-5] + '.mp3'
                print to_ffmpeg

                # DO FFMPEG TRANSCODE HERE
                #command_string = 'ffmpeg -i '+to_ffmpeg+' -qscale:a 0 '+output_name
                #os.system(command_string)

firstrun = False
directory = '/Volumes/Share/HD/Music/Files'
destination_folder = '/tmp'

savefile = directory+'/.seen'

if not firstrun:
    seenfolders = pickle.load(open( savefile,'rb'))
else:
    seenfolders = []


folders = os.listdir(directory)

to_transcode = []

for folder in folders:
    if folder[0] != '.' and folder not in seenfolders:
        to_transcode.append(folder)

# Do transcoding here

print 'Need to transcode ' + str(len(to_transcode)) + ' folders'
for folder in to_transcode:
    doTranscode(folder)
    seenfolders.append(folder)
    #if not firstrun:
    #    print folder

# Don't save changes yet so we can keep testing
#pickle.dump(seenfolders, open( savefile,'wb'))