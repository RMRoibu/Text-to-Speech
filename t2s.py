import os
import sys



text_path = sys.argv[1]
sound_path = sys.argv[2]
texts=os.listdir(text_path)
to_convert=[]
for i in range(0,len(texts)):
    with open(os.path.join(text_path,texts[i]),'r') as f:
        to_convert.append(f.readlines())




