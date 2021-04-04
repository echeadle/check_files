import os
import re

for folderName, subfolders, filenames in os.walk('/home/echeadle'):
    #print('The current folder is ' + folderName)
    subfolders[:] = [f for f in subfolders if not f in ['anaconda3','snap','venv','temp']]
    subfolders[:] = [f for f in subfolders if not f.startswith('.')]
    for subfolder in subfolders:
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        pass

    filenames[:] = [f for f in filenames if  not f.startswith('.')]
    filenames[:] = [f for f in filenames if  not f.startswith('__')]
    for filename in filenames:
       my_comma = re.findall(',', filename)
       if ',' in my_comma:
          print('FILE INSIDE ' + folderName + ': '+ filename)
    #print('')