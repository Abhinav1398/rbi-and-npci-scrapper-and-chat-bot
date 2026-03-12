import os
import hashlib

STATE_FILE = "monitor/state.txt"

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def detect_changes(folder):

    current = {}

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        current[file] = file_hash(path)

    return current