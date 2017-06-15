import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\IBM_ADMIN\Downloads\prank\prank")
    print(file_list)
    # what is the current working directory (cwd)?
    saved_path = os.getcwd()   
    print("Current Working Directory is: " + saved_path)
    # change cwd
    os.chdir(r"C:\Users\IBM_ADMIN\Downloads\prank\prank")
  
    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name: "+file_name)
        print("New Name: "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    # reset the cwd
    os.chdir(saved_path)

rename_files()

