import os
import shutil

#Make directory
directory = "directory1"

parent_dir = "C:/Users/Merlin Warner-Huish/PycharmProjects/Merlin/"

path = os.path.join(parent_dir, directory)

try:
    os.mkdir(path)
except Exception as e:
    print('error',e)

print('A piece of code after the error')
print("Directory " + directory + " created.")


#Move to directory
shutil.move('C:/Users/Merlin Warner-Huish/hi.txt.txt', directory)


#Copy files
src = 'C:/Users/Merlin Warner-Huish/hey.txt'
dst = 'C:/Users/Merlin Warner-Huish/PycharmProjects/Merlin'
shutil.copy(src, dst)

