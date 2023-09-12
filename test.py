import os
import time
import sys

#Directory path entered from command line argv[1]
dir_path = sys.argv[1] if len(sys.argv) > 1 else '.'

#creating dictionary for current dir list
head = dict ([(f, None) for f in os.listdir (dir_path)])
while 1:
        # iterating dictionary
        next = dict ([(f, None) for f in os.listdir (dir_path)])
        added = [f for f in next if not f in head] # new element added
        removed = [f for f in head if not f in next] #element removed
        # get the current dir path
        mydir = os.getcwd() 
        mydir_new = os.path.join(mydir,dir_path)
        if added:
            file_path = os.path.join(mydir_new,added[0])
            #print("file_path: ",file_path)
            if os.path.isfile(file_path):
                print("%s File created: " %time.asctime(time.localtime()),",".join(added))
                head = next # assigning new value to head
            else:
                if os.path.isdir(file_path):
                    print("%s Dir created: " %time.asctime(time.localtime()),",".join(added))
                    head = next # assigning new value to head
        elif removed:
            print("%s File/Dir Removed: " %time.asctime(time.localtime()),",".join(removed))
            head = next # assigning new value to head