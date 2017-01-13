import os, csv
import shutil #for moving files
import datetime as dt

os.chdir('E:\\')
if 'scan backup' not in os.listdir(os.getcwd()):
    os.mkdir('scan backup')

SCAN_BK = os.path.join('E:\\','scan backup')
CLIENT_FOLDER_PATH = 'E:\\Formerly Backup 01092016\\^ current PWIS 2015\\PROFESSIONAL WOMEN\'s INVESTMENT SERVICE\\AAA CLIENT FILES'
SCAN_LOG = os.path.join(SCAN_BK,'scan_log.csv')

f = open(SCAN_LOG,'w')
f.close()

os.chdir(CLIENT_FOLDER_PATH)


# creating a dict of client names and their filepaths

clientfolders = {folder:os.path.join(os.getcwd(), folder) for folder in os.listdir(os.getcwd())
         if os.path.isdir(os.path.join(os.getcwd(), folder))}

os.chdir('Z:\\')

#creating a list of scanned file names with extensions

scannedfiles = [file for file in os.listdir(os.getcwd())
         if os.path.isfile(os.path.join(os.getcwd(), file))]

f = open(SCAN_LOG,'a',newline='')
w = csv.writer(f)

for file in scannedfiles():
    filemoved = False
    for folder in list(clientfolders.keys()):
        for i in folder.split(' '):
            if i.upper() in file.upper() and len(i)>3:
                os.chdir(clientfolders[folder])

                if 'scanned files' not in os.listdir(os.getcwd()):
                    os.mkdir('scanned files')

                os.chdir(os.path.join(os.getcwd(),'scanned files'))

                #shutil.move(os.path.join('E:\\',file), os.path.join(os.getcwd(),file))          # moves files if they find a match

                print(os.path.join('E:\\',file)+' will be moved to: \t'+os.path.join(os.getcwd(),file))     #remove this if nothing looks fishy
                w.writerow([dt.datetime.now().isoformat(),file,folder,os.path.join(os.getcwd(),file)])


                filemoved=True
                break # only breaks out of innermost loop

        if filemoved == True:
            break

f.close()


