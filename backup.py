import os
import shutil
import hashlib
import hash
import zip
import delete_leftovers as dl

# Set the paths to the original and backup folders
original_path = 'f:/Vlad'
backup_path = 'f:/Backup/Backup_Vlad'
new_backup_path = 'f:/Backup'

# Check for leftover files in the backup path
dl.delete_leftover_files(original_path, backup_path)

# Walk through the folders and compare each file
for root, dirs, files in os.walk(original_path):
    # Calculate the corresponding path in the backup folder
    backup_root = root.replace(original_path, backup_path, 1)
    
    # Create any missing directories in the backup folder
    for d in dirs:
        backup_dir = os.path.join(backup_root, d)
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
    
    # Compare each file and copy it if necessary
    for f in files:
        original_file = os.path.join(root, f)
        backup_file = os.path.join(backup_root, f)

        if not os.path.exists(backup_file):
            shutil.copy2(original_file, backup_file)
        # else:
        #     if hashlib.sha256(open(original_file, 'rb').read()).hexdigest() != \
        #        hashlib.sha256(open(backup_file, 'rb').read()).hexdigest():
        #         shutil.copy2(original_file, backup_file)
        
        else:
            if hash.compare_hashes(original_file, backup_file) != "0%":
                shutil.copy2(original_file, backup_file)

# Archive the backup_path root folder
if os.path.exists(backup_path):
    zip.archive(backup_path, new_backup_path)