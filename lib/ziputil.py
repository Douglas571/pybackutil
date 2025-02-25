from pathlib import Path
from zipfile import ZipFile
from os import walk as dirwalk, path as ospath

def single_compress(src_filepath: str, target_handle_path: str):
    target_fullpath = Path(target_handle_path).resolve()
    handle = ZipFile(target_fullpath, 'w')
    handle.write(src_filepath)
    handle.close()

def dir_compress(src_dirpath: str, target_handle_path: str):
    target_fullpath = Path(target_handle_path).resolve()
    handle = ZipFile(target_fullpath, 'w')

    for root, files, dirs in dirwalk(src_dirpath):
        for name in dirs:
            handle.write(ospath.join(root, name))
        for name in files:
            handle.write(ospath.join(root, name))
    
    handle.close()

def bulk_compress(src_filelist: str, target_handle_path: str):
    target_fullpath = Path(target_handle_path).resolve()
    handle = ZipFile(target_fullpath, 'w')

    for itempath in src_filelist:
        handle.write(itempath)
    
    handle.close()

def extract_all(src_handle_path: str, target_dirpath: str):
    target_fullpath = Path(target_dirpath).resolve()
    src_fullpath = Path(src_handle_path).resolve()
    handle = ZipFile(src_fullpath, 'r')

    handle.extractall(target_fullpath)
    handle.close()