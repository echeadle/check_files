	
# Import the os module, for the os.walk function
import hashlib
import os
import re

the_hash = hashlib.sha256()
rootDir = '/home/echeadle'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    fileList[:] = [f for f in fileList if not f.startswith('.')]
    fileList[:] = [f for f in fileList if not f.startswith('__')]
    for fname in fileList:
        full_file_path = os.path.join(dirName, fname)         
        if os.path.isfile(full_file_path):
            with open(full_file_path, 'rb') as fn:
                for line in fn.readlines():
                    the_hash.update(line)
            print(f"{full_file_path:50},{fname:30},{the_hash.hexdigest():30}")
    # Remove the first entry in the list of sub-directories
    # if there are any sub-directories present
    subdirList[:] = [d for d in subdirList if not d.startswith('.')]
    subdirList[:] = [d for d in subdirList if not d in ['anaconda3', 'venv','temp']]