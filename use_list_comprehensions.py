import hashlib
import os
import re


the_hash = hashlib.sha256()

for root, dirs, files in os.walk('/home/echeadle', topdown=True):
    print(root, dirs, files)
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    dirs[:] = [d for d in dirs if not d.startswith('__')]
    dirs[:] = [d for d in dirs if not d in ['anaconda3', 'venv','temp', 'google-cloud-sdk']]
    files[:] = [f for f in files if not f.startswith('.')]
    files[:] = [f for f in files if not f.startswith('__')]

    print(root, dirs, files)
    for dir in dirs:
        for file in files:
            print(f'file {file}')
            full_file_path = os.path.join(root, file)        
            if os.path.isfile(full_file_path):
                with open(full_file_path, 'rb') as fn:
                    for line in fn.readlines():
                        the_hash.update(line)
                print(f"{full_file_path:50},{file:30},{the_hash.hexdigest():30}")

 