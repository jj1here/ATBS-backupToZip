#! python3
#copies an entire folder and its content into a Zip file whose filename increments

import zipfile, os

def backupToZip(folder) :
    
    folder = os.path.abspath(folder) # make sure folder is absolute

    #figures out filename
    number = 1
    while True :
        zipFileName = os.path.basename(folder)+'_'+str(number) + '.zip'

        if not os.path.exists(zipFileName) :
            break
        number += 1

    # create zip file
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # walk the entire folder tree and compress the files
    for foldername, subfolders, filenames in os,os.walk(folder) :
        print(f'Adding files in {foldername}...')
        # add the current folder to the zip file
        backupZip.write(foldername)

        # add all files in this folder to the zip file
        for filename in filenames :
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip') :
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done.")

# backupToZip('~/Documents/Python\ /Practice/')

    


