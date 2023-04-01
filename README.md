# Backup_Script

This script takes two paths (original and backup) and compares them. 
If there is no file in the backup path, they are first created then copied from the original path.
If there are files in the backup path, they are compared by their hash. 
If there are differences in the hash, the file from the original path is copied to the backup path. Same hash, nothing happens.
After every file is compared, the backup main folder is zipped with the current date. 
