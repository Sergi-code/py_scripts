import os


folder_to_track = "C:/Users/sergi/Desktop/oldFolder"
folder_destination = "C:/Users/sergi/Downloads"

for filename in os.listdir(folder_to_track):
    src = folder_to_track + "/" + filename;
    paths = filename.split("_")
    dir = os.path.join(folder_destination, *paths)
    try:
        os.rename(src, dir)
    except FileNotFoundError:
        os.mkdir(os.path.dirname(dir))
        os.rename(src, dir)
    except FileExistsError:
        pass
