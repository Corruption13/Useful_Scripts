import os
import zipfile

path = input('Enter the directory: ')
path = os.path.abspath(os.path.normpath(os.path.expanduser(path)))
for folder in os.listdir(path):
    zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(os.path.join(path, folder)):
        for filename in files:
            zipf.write(os.path.abspath(os.path.join(root, filename)), arcname=filename)
    zipf.close()
