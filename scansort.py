import os, csv
import shutil #for moving files
import datetime as dt

os.chdir('E:\\')
if 'scan backup' not in os.listdir(os.getcwd()):
    os.mkdir('scan backup')

SCAN_BK = os.path.join('E:\\','scan backup')
CLIENT_FOLDER_PATH = 'E:\\Formerly Backup 01092016\\^ current PWIS 2015\\PROFESSIONAL WOMEN\'s INVESTMENT SERVICE\\AAA CLIENT FILES'
SCAN_LOG = os.path.join(SCAN_BK,'scan_log'+dt.datetime.now().isoformat().replace(':','')[:17]+'.csv')

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

def parse_files():
    for file in scannedfiles():

        matchlist=[]

        surnames = [(folder.split(', ')[0],folder.split(', ')[1][0],folder) for folder in list(clientfolders.keys())]
        for i,j,k in surnames:
            if i.upper() in file.upper():
                matchlist.append((i,j,k))         #now contains folder

        if len(matchlist)==1:
            move_decision(matchlist[0][2],file)             #moves full 'folder' name to decision

        if len(matchlist)>1:
            if len(matchlist[0][0]!=len(matchlist[1][0])):      #if one surname is longer, take the longest
                longest_surname = [('','','')]
                for tup in matchlist:
                    if len(tup[0])>len(longest_surname[0][0]):
                        longest_surname = [tup]

                move_decision(longest_surname[0][2], file)



            if len(matchlist[0][0]==len(matchlist[1][0])):
                newmatchlist=[]
                for tup in matchlist:
                    matchstring = str(tup[0]) + str(tup[1])                        #looking for SmithJ, Smith W etc
                    if matchstring.upper() in file.upper():
                        newmatchlist.append(tup)

                if len(newmatchlist)==1:
                    move_decision(newmatchlist[0][2],file)
                else:
                    newmatchlist = []
                    for tup in matchlist:
                        matchstring = str(tup[0]) + ' ' + str(tup[1])             # Smith J, Smith W etc
                        if matchstring.upper() in file.upper():
                            newmatchlist.append(tup)
                    if len(newmatchlist) == 1:
                        move_decision(newmatchlist[0][2], file)

                    else:
                        print("couldn't move: "+str(matchlist))




def move_decision(folder, file):


    os.chdir(clientfolders[folder])

    if 'scanned files' not in os.listdir(os.getcwd()):
        os.mkdir('scanned files')

    os.chdir(os.path.join(os.getcwd(), 'scanned files'))

    # shutil.move(os.path.join('E:\\',file), os.path.join(os.getcwd(),file))          # moves files if they find a match

    print(os.path.join('E:\\', file) + ' will be moved to: \t' + os.path.join(os.getcwd(),
                                                                              file))  # remove this if nothing looks fishy
    w.writerow([dt.datetime.now().isoformat(), file, folder, os.path.join(os.getcwd(), file)])




if __name__=='__main__':
    parse_files()

f.close()