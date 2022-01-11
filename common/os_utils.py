import hashlib
import os


def make_directory(path):
    os.makedirs(path, exist_ok=True)


def md5_file(path):
    hash_md5 = hashlib.md5()
    if not os.path.exists(path):
        return None

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
