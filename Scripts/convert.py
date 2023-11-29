from PIL import Image

img = Image.open('test1.jpg')

img_array = img.load()
w, h = img.size
# print(w, h)
for x in range(w):
    for y in range(h):
        rgb = img_array[x, y]
        img_array[x, y] = (rgb[2], rgb[1], rgb[0]) # convert from bgr to rgb

img.save('testout1.jpg')