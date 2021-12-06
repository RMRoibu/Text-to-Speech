import os
import sys
from gtts import gTTS

# Wrote this to have a clear folder to work on
def clearResultFolder(target):
    for filename in os.listdir(target):
        os.unlink(os.path.join(target,filename))

language = 'en'
to_convert=[]
RED_COLOR="\033[0;31m"
RESET_COLOR="\033[0m"

if(len(sys.argv)<3):
    print(RED_COLOR+"The script requires 2 arguments!"+RESET_COLOR)
    exit()

text_path = sys.argv[1]
sound_path = sys.argv[2]
clearResultFolder(sound_path)

filesToReadFrom=[]
for rootFolder,subdirectories,files in os.walk(text_path):
    for file in files:
        filesToReadFrom.append(os.path.join(rootFolder,file))


for filePath in filesToReadFrom:
     with open(filePath,'r') as file:
        rawText = file.read()
        if(rawText!=""):
            to_convert.append(rawText)

name_count=0
for i in to_convert:
    the_text=to_convert[name_count]
    name_count+=1
    conversion= gTTS(text=the_text, lang=language, slow=False)
    conversion.save(os.path.join(sound_path,"S"+str(name_count)+".mp3"))



