#Renames all files in a folder to 1-x ordered by their creation date
import os

def sorted_dir(folder):
    def getctime(name):
        path = os.path.join(folder, name)
        return os.path.getctime(path)
    return sorted(os.listdir(path), key=getctime)

path = os.path.abspath("D:\Desktop\gp")
i = 0
for file_name in sorted_dir(path):
    _, ext = os.path.splitext(file_name)
    print (file_name + " - " + str(i)+ext)    
    os.rename(os.path.join(path,file_name), os.path.join(path, str(i) + ext)
    i += 1
    
print(str(i-1) + " files.")

