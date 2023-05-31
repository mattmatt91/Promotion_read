import os

root = 'C:\Users\admin\Desktop\data_PHD\safe_combustion'

for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))