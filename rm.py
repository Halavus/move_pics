import os

def rm(directory_path):
    content=os.listdir(directory_path)
    for i in content:
        file_path=''.join([directory_path, i])
        os.remove(file_path)
        print i, 'successfully removed'

    print '\n'
