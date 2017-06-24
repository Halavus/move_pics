import os
# because of the for loop, filename(s) has to be in a python list
def touch(lst, times=None): 
    for i in lst:
        with open(i, 'a'):
            os.utime(i, times)
