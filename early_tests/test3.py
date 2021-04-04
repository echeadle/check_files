import os

def list_files(filepath, filetype):
    paths = []

    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return(paths)


my_files_list = list_files('/home/echeadle', '.pdf')
for file in my_files_list:
    print(file)