import os

os.system('python setup.py install --record files.txt')
os.system('cat files.txt | xargs rm -rf')
