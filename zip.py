import os
import zipfile
import datetime

def archive(backup_root, new_backup_path):
    backup_path = os.path.dirname(backup_root)
    if backup_path:
        now = datetime.datetime.now()
        archive_name = os.path.basename(backup_root)
        backup_archive = os.path.join(new_backup_path, f"{archive_name}_{now.strftime('%d_%m_%Y')}.zip")
        with zipfile.ZipFile(backup_archive, "w") as zf:
            for root, dirs, files in os.walk(backup_root):
                for f in files:
                    file_path = os.path.join(root, f)
                    arcname = os.path.relpath(file_path, backup_path)
                    zf.write(file_path, arcname=arcname)
