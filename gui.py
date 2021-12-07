
import tkinter as tk
import os
from gtts import gTTS
from playsound import playsound
import string
import random
letters = string.ascii_letters + string.digits
textToplay = None


def generateTemporaryFileName(fileNameSize=10):
    return '.'+''.join(random.choice(letters) for i in range(fileNameSize))+".mp3"

def get_text_and_play():
    global entry_text
    tmpFileName = generateTemporaryFileName()
    to_convert= gTTS(text=entry_text.get(), lang='en', slow=False)
    to_convert.save(tmpFileName)
    playsound(tmpFileName)
    os.remove(tmpFileName)

root = tk.Tk()
root.geometry('400x100')
root.title("T2S App")

entry_text = tk.StringVar()
entry = tk.Entry(root, width=200, textvariable=entry_text)
entry.pack()

button = tk.Button(root, text="Play", command=get_text_and_play)
button.pack()
root.mainloop()

list=list(os.listdir(os. getcwd()))
counter=0
for i in list:

    if "mp3" in list[counter]:
        os.remove(list[counter])
        counter+=1