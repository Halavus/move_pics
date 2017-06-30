#!/usr/bin/python

import os
import sys
import numbers
from rm import rm as rm
from touch import touch as touch

help_string = (
        "Usage:" 
        "\n"
        "main.py [SOURCE_DIR] [LIST_OF_ARTICLES.csv] [TO_KEEP.d] "
        "[TO_TRASH.d] "
)

if sys.argv[1] in ("--help", "-help", "help", "-h"):
    print help_string
    sys.exit()
else:
    pass

cwd = ""
def mkpath(arg, wd=cwd):
    path = ''.join([wd, arg])
    return path


cwd = mkpath('/', wd=os.getcwd())

# ### Global Variables ###


# Paths #
source_dir = mkpath(sys.argv[1])
input_csv = mkpath(sys.argv[2])
to_keep_dir = mkpath(sys.argv[3])
to_trash_dir = mkpath(sys.argv[4])
ls_source_dir = os.listdir(source_dir)

with open(input_csv, 'rb') as f:
    articles_list = [i[:7] for i in f]

articles_list = [i.replace('\r\n', '') for i in articles_list]


# ### Classes ###
class Picture:
    '''A class defined by 3 attributes.

    -the filename of the picture
    -the article number (anb) which has to beginn with a 'A'
    and not 'a'. format: 'A123456'
    -the path of the picture
    '''

    def __init__(self, filename, source_dir=source_dir):
        self.filename = filename
        anb_small = filename[:7]

        ''' Check if the file really contains the pattern
        AXXXXXX... X should be integers
        '''
        try:
            [isinstance(int(x), numbers.Number) for x in anb_small[1:]]
            # The A-Nb. evt has 'a' instead of 'A'
            self.anb = anb_small.replace('a', 'A')

        except ValueError:
            self.anb = None

        self.path = mkpath(self.filename, wd=source_dir)

# ### Do the job ###
'''
# emptying directories, for debug purpose - TODO add option
rm(to_keep_dir)
rm(to_trash_dir)
'''
# recreate .gitkeep
touch([mkpath(".gitkeep", wd=to_keep_dir)])


images = [Picture(i) for i in ls_source_dir]


# NOTE debug
logs = mkpath("logs", wd=cwd)
debug = open(logs, 'w')

'''
for item in images:
    debug.write("%s\n" % item.filename)
'''

for pic in images:
    if pic.anb in articles_list or not pic.anb:
        try:
            dest_path = mkpath(pic.filename, wd=to_keep_dir)
            os.link(pic.path, dest_path)
        except OSError:
            pass
    else:
        try:
            dest_path = mkpath(pic.filename, wd=to_trash_dir)
            os.link(pic.path, dest_path)
        except OSError:
            pass

'''
# export logfiles
# TODO fix the weird behavior of touch needing the path be in list
success_log = [mkpath("current_pictures.txt")]
touch(success_log)
to_trash_log = [mkpath("not-linked_pictures.txt")]
touch(to_trash_log)

# export success into file
log = open(success_log[0], 'w')
for item in success:
    log.write("%s\n" % item)

# export to_trash into file
log = open(to_trash_log[0], 'w')
for item in to_trash:
    log.write("%s\n" % item)
'''
'''
# ### Debug ###
print 'DEBUG'
print '-' * 20
print '\n'
print 'From source dir: ', source_dir
# print 'This is the python-generated articles_list: ', articles_list
#print 'This is the list of images found in source dir: ', ls_source_dir

print 'successfully linked picture(s): ', success
#print 'Those files will be to trash: ', to_trash
'''
