import os
from PIL import Image

path ='C:\\ECS289G\\HQSAM'

def get_filelist(dir):
 
    Filelist = []
    Filenamelist = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(os.path.join(home, filename))
            Filenamelist.append(filename)
 
    return Filenamelist
 
if __name__ =="__main__":
 
    Filelist = get_filelist(dir)
    for file in  Filelist :
        img = Image.open(file)
        img_array = img.load()
        w, h = img.size
        for x in range(w):
            for y in range(h):
                rgb = img_array[x, y]
                img_array[x, y] = (rgb[2], rgb[1], rgb[0]) # convert from bgr to rgb

        img.save(file)
    