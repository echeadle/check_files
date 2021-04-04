import hashlib
import os
import re


the_hash = hashlib.sha256()

full_file_path = '/home/echeadle/Projects/Udemy-100DaysOfCode/test_file6.py'

if os.path.isfile(full_file_path):
    with open(full_file_path, 'rb') as fn:
        for line in fn.readlines():
            the_hash.update(line)

print(f"{full_file_path:50} {the_hash.hexdigest():30}")