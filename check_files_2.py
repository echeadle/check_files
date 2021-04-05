#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2021-04-04
Purpose: Rock the Casbah
"""

import argparse
import hashlib
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()

def get_skipped_dirs():
    return list(('anaconda3','snap','venv','temp'))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')

    skip_dirs = get_skipped_dirs()
    root_dir = '/home/echeadle'

    for folderName, subfolders, filenames in os.walk(root_dir):
        #print('The current folder is ' + folderName)
        subfolders[:] = [f for f in subfolders if not f in skip_dirs]
        subfolders[:] = [f for f in subfolders if not f.startswith('.')]
        for subfolder in subfolders:
            #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            pass
        filenames[:] = [f for f in filenames if  not f.startswith('.')]
        filenames[:] = [f for f in filenames if  not f.startswith('__')]
        #filenames[:] = [f for f in filenames if  re.findSall('test', f, flags=re.IGNORECASE)]
        for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': '+ filename)
            full_file_path = os.path.join(folderName, filename)      
            the_hash = hashlib.sha256()   
            if os.path.isfile(full_file_path):
                with open(full_file_path, 'rb') as fn:
                    for line in fn.readlines():
                        the_hash.update(line)
                fn.close()
                print(f"{folderName},{filename},{the_hash.hexdigest()}")

# --------------------------------------------------
if __name__ == '__main__':
    main()
