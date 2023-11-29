from PIL import Image


def load_resize(filename, size=None, size2=344, scale=None, keep_asp=False):
    img = Image.open(filename)
    if size is not None:
        if keep_asp:
            size2 = int(size * 1.0 / img.size[0] * img.size[1])
            img = img.resize((size, size2), Image.ANTIALIAS)
        else:
            img = img.resize((size, size2), Image.ANTIALIAS)

    elif scale is not None:
        img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)),
                         Image.ANTIALIAS)
    # img = np.array(img).transpose(2, 0, 1)
    # img = torch.from_numpy(img).float()
    return img


img2 = load_resize('testout.jpg', size=512, keep_asp=True) # resized background to 512, 344
img = Image.open('test1.jpg')

img_array = img.load()
img_array_b = img2.load()
w, h = img.size

for x in range(w):
    for y in range(h):
        rgb = img_array[x, y]
        rgb_b = img_array_b[x, y]
        if rgb_b[0] >= 235 and rgb_b[1] >= 235 and rgb_b[2] >= 235:
            img_array_b[x, y] = img_array[x, y]

img2.save('testoutfinal.jpg')