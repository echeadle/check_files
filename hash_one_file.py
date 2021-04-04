import hashlib
import sys

file_name = sys.argv[1]
the_hash = hashlib.sha256()
with open(file_name, 'rb') as fn:
    for line in fn.readlines():
        the_hash.update(line)
print(the_hash.hexdigest())