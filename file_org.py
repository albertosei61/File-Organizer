import os
import shutil
from file_ext import dir_dict

dir_path = "C:\\Users\\username\\"


for key in dir_dict:
    folder_path = os.path.join(dir_path, key)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for item in os.listdir(dir_path):
    item_path = os.path.join(dir_path, item)
    if os.path.isfile(item_path):
        file_extension = os.path.splitext(item)[1]
        for folder, extensions in dir_dict.items():
            if file_extension in extensions:
                new_path = os.path.join(dir_path, folder, item)
                shutil.move(item_path, new_path)
                break
    elif os.path.isdir(item_path):
        for folder, extensions in dir_dict.items():
            for extension in extensions:
                if extension in item:
                    shutil.move(item_path, new_path)
                    break
