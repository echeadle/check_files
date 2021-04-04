import hashlib
import os
import re


the_hash = hashlib.sha256()

match = re.compile(r'\..*')
for root, dirs, files in os.walk('/home/echeadle'):
    for dir in dirs:
        if match.findall(dir):
            continue
        for file in files:
            full_file_path = os.path.join(root, file)   
            if match.findall(root):
                continue        
            if os.path.isfile(full_file_path):
                with open(full_file_path, 'rb') as fn:
                    for line in fn.readlines():
                        the_hash.update(line)
                print(f"{full_file_path:50},{file:30},{the_hash.hexdigest():30}")
                    
                        #print(os.path.join(root, file))
                #print(f"root is: {root}\ndirs is:{dirs}\n\n")

 