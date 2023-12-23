import os
import shutil 

folder_list = []
folder_info = {}

root = "/"
root = os.path.abspath(root)

for folder, subfolders, files in os.walk(root):
    for file in files:
        file_path = os.path.join(folder, file)
        # folder_list.append(file_path)
        try:
            folder_info[file_path] = os.path.getsize(file_path)
        except:
            folder_info[file_path] = 0

# biggest_folder_path = max(folder_list, key = os.path.getsize())



count = 0
for file in sorted(folder_info, key=folder_info.get, reverse=True):
    count += 1
    print(file, folder_info[file])
    if count == 10:
        break
