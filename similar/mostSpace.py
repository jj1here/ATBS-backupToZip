#! python3
# search folders for the files using the most disk space


import os, shutil

def mostSpace(folder) :

    #folder path
    folder = os.path.abspath(folder)

    # for size of each file
    space = 0
    #size of largest file
    maxSize = 0
    #path of bigeest file
    bigFile = ""

    # walks through the entire folder
    for foldername, subfolders, filenames in os.walk(folder) :
        # checks the size of each file
        for file in filenames:
            space = os.stat(os.path.join(foldername,file)).st_size

            # updates max size
            if space > maxSize :
                maxSize = space
                bigFile = os.path.join(foldername, file)
    
    print(f'The biggest folder is {bigFile} with a size of {maxSize} bytes')

mostSpace("Automate the boring stuff")
    

