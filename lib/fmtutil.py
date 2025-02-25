from glob import iglob
from pathlib import Path
from lib.config import OS_PATH_DELIM

def normalize_loc(item_path: str):
    return item_path.split(OS_PATH_DELIM)[-1]

def tree_of(dir_path: str):
    fresh = True
    dir_count = 0
    file_count = 0
    
    for item in iglob(dir_path + "/**", recursive=True):
        concrete = Path(item)

        if fresh:
            print(f"{item} [ROOT]")
            fresh = not fresh
            continue

        if concrete.is_dir():
            dir_count += 1
            print(f"{'\t' * item.count(OS_PATH_DELIM)} {normalize_loc(item)} [DIR]")
        else:
            file_count += 1
            print(f"{'\t' * item.count(OS_PATH_DELIM)} {normalize_loc(item)} [FILE]")

    print(f"\n{file_count} files, {dir_count} directories\n")