'''Hash function for two files which paths are given'''

from difflib import SequenceMatcher
import hashlib

def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
    
    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()

def compare_hashes(fileName1, fileName2):
    h1, h2 = hash_file(fileName1, fileName2)
    diff = 0
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            diff += 1
    percentage_diff = diff / len(h1) * 100
    return f"{percentage_diff:.2f}%"