from os import getcwd, scandir, rename, makedirs
from os.path import splitext, exists, join, expanduser

# Source directory (where script is placed)
SOURCE_DIR = getcwd()
CURRENT_USER = expanduser("~")

# Destination folders
DOCUMENTS = join(CURRENT_USER, "Documents")
PICTURES = join(CURRENT_USER, "Pictures")
MUSIC = join(CURRENT_USER, "Music")
VIDEOS = join(CURRENT_USER, "Videos")

# Extension mapping
FOLDERS = [
    {".txt": DOCUMENTS},
    {".pdf": DOCUMENTS},
    {".png": PICTURES},
    {".jpg": PICTURES},
    {".jpeg": PICTURES},
    {".webp": PICTURES},
    {".svg": PICTURES},
    {".mp3": MUSIC},
    {".wav": MUSIC},
    {".mp4": VIDEOS},
    {".mov": VIDEOS},
    {".avi": VIDEOS},
    {".gif": VIDEOS},
]

def get_destination(extension):
    for item in FOLDERS:
        if extension in item:
            return item[extension]
    return None

def move_file(file_name):
    name, ext = splitext(file_name)
    destination = get_destination(ext.lower())

    if destination:
        # Create folder if it doesn't exist
        if not exists(destination):
            makedirs(destination)

        src = join(SOURCE_DIR, file_name)
        dst = join(destination, file_name)

        try:
            rename(src, dst)
            print(f"Moved: {file_name} → {destination}")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")

def main():
    for file in scandir(SOURCE_DIR):
        if file.is_file():
            move_file(file.name)

if __name__ == "__main__":
    main()
