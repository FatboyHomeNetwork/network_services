import os
import sys
import io
import shutil
from datetime import datetime

def build_hash_dic(path): 
    
    hash_dic = {}
    
    for subdir, dirs, files in os.walk(path):
        
        for file in files:
            abs_path = os.path.join(subdir,file)
            rel_path = abs_path.replace(path,'')
            last_mod_time = str(os.path.getmtime(abs_path))
            
            hash_dic[last_mod_time + rel_path ] = [abs_path, rel_path] 
    
    return hash_dic
    

def build_log_line(*args):
    # (\n) 
    # (message\n)
    # (action: message\n)
    
    if len(args) == 0:
        return '\n'
    if len(args) == 1:
        return str(args[0]) + '\n'
    if len(args) == 2:
        return  (args[0] + ':').ljust(12) + args[1] + '\n'


def unicode_free(string):
    return ''.join([i if ord(i) < 128 else ' ' for i in string])
    

def run(original, image, log_file):
        
    start = datetime.now()
    
    log_file = open(log_file, 'a')
    log_file.write(build_log_line('Start', start.strftime('%c')))
    
    original_dic = build_hash_dic(original)
    image_dic = build_hash_dic(image)


    # files in the image but not in the original. This means the files have been deleted or updated from 
    # original source, so delete them from the image 
    for k, v in image_dic.items():
        if not k in original_dic:
            
            os.remove(v[0])
            
            log_file.write(build_log_line('Old-Del', unicode_free(v[0])))


    # The original file is not in the current image. This could because 1) the file is new, 
    # or 2) the file has been updated - last modified is past of out hash. Either way, lets copy 
    # it over 
    for k, v in original_dic.items():
        if not k in image_dic:
            
            new_image_dir = os.path.dirname( image +  v[1])
            os.makedirs(new_image_dir, exist_ok=True)
            shutil.copy2(v[0], new_image_dir)
            
            log_file.write(build_log_line('New-Update', unicode_free(v[0])))

    
    diff_sec = (datetime.now() - start).total_seconds()
    number_files = len(original_dic.items())
        
    log_file.write(build_log_line('Time: %.6s' %str(diff_sec/60) + ' minutes'))
    log_file.write(build_log_line("{:,}".format(number_files) + ' files processed'))
    log_file.write(build_log_line())
    
    log_file.close()

    ## Add soem kind of exception gn here. 

#
# main()
#

if len(sys.argv) == 4:
    # 'fatboy_sync.py' 'original path' 'image folder' 'log file path'
    run(sys.argv[1], sys.argv[2], sys.argv[3])
