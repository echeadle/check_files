import os
#import re

num = 0
newdirs =[]
for root, dirs, files in os.walk('/home/echeadle'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    dirs[:] = [d for d in dirs if not d in ['anaconda3', 'venv','temp', 'google-cloud-sdk']]
    if num > 30:
        break
    for dir in dirs:
        print(dir)
        for file in files:
            print("\t\t", file)
    num += 1