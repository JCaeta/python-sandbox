from os import listdir
from os.path import join, isfile, splitext
        
folder = "./folder1"
files = [f for f in listdir(folder) if isfile(join(folder, f))]

list_png_files = []
for file in files:
    split_file = splitext(file)
    if split_file[1] == ".png":
        list_png_files.append(file)

print(list_png_files)



