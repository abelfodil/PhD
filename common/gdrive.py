import os.path
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from tqdm import tqdm

from common.os_utils import make_directory, md5_file

_BASE_LOCAL_GDRIVE_PATH_PREFIX = f"{os.getcwd()}/gdrive_data"


def _get_drive_service():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)
    return drive


def _is_folder(gfile):
    return gfile['mimeType'] == 'application/vnd.google-apps.folder'


def _download_file(file, destination):
    local_hash = md5_file(destination)
    remote_hash = file.get('md5Checksum')
    if local_hash != remote_hash:
        file.GetContentFile(destination)


def download_file(file_id, destination):
    drive = _get_drive_service()
    file = drive.CreateFile({'id': file_id})
    _download_file(file, destination)


def _recursively_list_files(folder_id, destination, drive):
    flat_file_list = []
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    for f in file_list:
        new_destination = f"{destination}/{f['title']}"
        if _is_folder(f):
            flat_file_list.extend(_recursively_list_files(f['id'], new_destination, drive))
        else:
            flat_file_list.append({"object": f, "path": new_destination})

    return flat_file_list


def download_drive_folder(folder_id, destination=None):
    drive = _get_drive_service()

    if destination is None:
        folder = drive.CreateFile({'id': folder_id})
        destination = f"{_BASE_LOCAL_GDRIVE_PATH_PREFIX}/{folder['title']}"

    print("Fetching file list...")
    file_list = _recursively_list_files(folder_id, destination, drive)
    print(f"Found {len(file_list)} files")

    print("Downloading files...")
    for file in tqdm(file_list):
        file_path = file['path']
        make_directory(os.path.dirname(file_path))
        _download_file(file['object'], file_path)

    return destination
