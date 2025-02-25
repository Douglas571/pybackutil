from pathlib import Path 
from os import stat as metaof
from datetime import datetime

def file_exists(file_path: str):
    solid = Path(file_path).resolve()
    return solid.is_file()

def dir_exists(dir_path: str):
    solid = Path(dir_path).resolve()
    return solid.is_dir()

def get_file_extension(file_path: str):
    return Path(file_path).resolve().__str__().split('.')[-1]

def get_item_creation_date(item_path:str):
    solid = Path(item_path).resolve()
    stamp = metaof(solid).st_birthtime
    return datetime.fromtimestamp(stamp).date()