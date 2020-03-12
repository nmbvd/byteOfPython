import os
import time
import zipfile

# 1. The files and directories to be backed up are
# specified in a list.
source = r"C:\Users\EGXXJXX\OneDrive - ODMAIL\123\doc\ericsson\tech document\project\山西联通\OSS信息表格\ENM"

# 2. The backup must be stored in a
# main backup directory
target_dir = r'C:\Users\EGXXJXX\Desktop\backup'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
#target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
target_dir1 = target_dir + os.sep + time.strftime('%Y%m%d')
comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = target_dir1+os.sep + time.strftime('%H%M%S')+'.zip'
else:
    target = target_dir1+os.sep + time.strftime('%H%M%S')+ '_' + comment.replace(' ', '_')+'.zip'




# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
if not os.path.exists(target_dir1):
    os.mkdir(target_dir1)

# 5. We use the zip command to put the files in a zip archive

basedir=os.path.split(source)[0]
with zipfile.ZipFile(target,'w') as myzip:
    for root, dirs, files in os.walk(source):
        for name in files:
            print(os.path.join(root, name))
            print(os.path.join(root, name)[4:])
            #myzip.write(os.path.join(root, name),os.path.join(root[len(basedir)+1:],name))

print('Successful backup to', target)



