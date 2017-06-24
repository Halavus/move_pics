#! py2
# -*- coding: utf-8 -*-

import os
import sys
from rm import rm as rm
from touch import touch as touch

# Usage:
# python util.py SOURCE/ LIST.ext DEST/

### Global Variables ###
cwd=''.join([os.getcwd(), '/'])

# Paths #
source_folder=''.join([cwd, sys.argv[1]])
source_articles_list=''.join([cwd, sys.argv[2]])
destination_folder=''.join([cwd, sys.argv[3]])

pics_list=os.listdir(source_folder)

articles_list=[]
with open(source_articles_list, 'rb') as f:
    for i in f:
        i=i[:7]
        articles_list.append(i)


### Classes ###
class Picture:
    '''A class defined by 3 attributes.

    -the filename of the picture
    -the article number (self.anb) which has to beginn with a 'A'
    and not 'a'. format: 'A123456'
    -the path of the picture
    '''

    def __init__(self, filename, source_folder=source_folder):
        self.filename=filename # A******.foo
        correct_A=filename.replace('a', 'A')
        self.anb=correct_A[:7]
        self.path=''.join([source_folder, self.filename])


### Functions ###

def replace(lst=articles_list):
    counter = 0
    for i in lst:                    
        lst[counter]=i.replace('\r\n','')
        counter+=1
replace()



### Do the job ###

# emptying dest Folder - TODO check if func removal on production 
rm(destination_folder)
# recreate .gitkeep
gitkeep=[''.join([destination_folder, ".gitkeep"])]
touch(gitkeep)

pictures=[]
for i in pics_list:
    item=Picture(i)
    pictures.append(item)

success=[]
not_linked=[]
for i in pictures:
    if i.anb in articles_list:
        success.append(i.filename)
        dest_path=''.join([destination_folder, i.filename])
        os.link(i.path, dest_path)

    else:
        not_linked.append(i.filename)



### Debug ###
print 'DEBUG'
print '-'*20
print '\n'
print 'From source folder: ', source_folder
#print 'This is the python-generated articles_list: ', articles_list
print 'This is the list of pictures found in source folder: ', pics_list

print 'successfully linked picture(s): ', success
print 'Those files were not linked: ', not_linked
