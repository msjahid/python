import os

'''
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return ("%3.1f %s" %(num, x))
        else:
            num /= 1024.0
            '''
'''
def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        num = file_info.st_size
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return ("%3.1f %s" %(num, x))
            else:
                num /= 1024.0
                '''
        #return convert_bytes(file_info.st_size)

file_path = "C:\Windows\System32\MRT-KB890830.exe"
if os.path.isfile(file_path):
    file_info = os.stat(file_path)
    num = file_info.st_size
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            print ("%3.1f %s" % (num, x))
            break;
        else:
            num /= 1024.0
