import os
import shutil

src="C:/Users/aaa/Documents/Test_File"
dest="C:/Users/aaa/Documents/File_Organiser"

list_of_files = os.listdir(src)

for file_name in list_of_files:
    
    name,ext = os.path.splitext(file_name)

    if ext == '':
        continue
    
    if ext in ['.png', '.jpg', '.pdf', '.gif', '.txt', '.xls']:
        path1 = src+'/'+file_name
        path2 = dest+'/'+ext
        path3 = dest+'/'+ext+'/'+file_name
        
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
            
        else:
            os.mkdir(path2) 
            shutil.move(path1,path3) 
        
        









