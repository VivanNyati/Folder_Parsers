import os

def folder_reader(folder_path):
    try:
        
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        files_without_extension = [f[:-4] for f in files if f.endswith('.pdf') or f.endswith('.txt')]
        
        for file in files_without_extension:
            print(file)
    except Exception as e:
        print(e, "\nRemember to put the correct path name.")

folder_reader(r"") # <--- Put path into here
