import os
import shutil

def delete_leftover_files(original_path, backup_path):
    for root, dirs, files in os.walk(backup_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(os.path.join(original_path, file)):
                try:
                    os.remove(file_path)
                except PermissionError:
                    print(f"Failed to delete file: {file_path}. Skipping.")