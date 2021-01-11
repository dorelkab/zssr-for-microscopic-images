import numpy as np
from matplotlib import pyplot as plt
import io
from PIL import Image as im

img = np.load("data\\data_label.npz")
lst=img.files

for i in range(2):
    for j in range(5):
        # item=img[lst[i]][j][0]
        # plt.imshow(item)
        # plt.axis('off')
        fig = plt.figure(frameon=False)
        fig.set_size_inches(img[lst[i]][j][0].shape[1] / 100, img[lst[i]][j][0].shape[0] / 100)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        ax.imshow(img[lst[i]][j][0], aspect='auto')
        # item = item * 255
        # item = item.astype(np.uint8)
        # data = im.fromarray(item)
        if(i==0):
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            imge = im.open(buf).convert('RGB')
            imge.save("data/Y/pic_" + str(j) + ".png")
            buf.close()
            # "Y/pic_" + str(j) + ".png", bbox_inches = 'tight'
        else:
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            imge = im.open(buf).convert('RGB')
            imge.save("data/X/pic_" + str(j) + ".png")
            buf.close()

        # img.shape
        # plt.ion()
        # plt.figure()
        # img = img.squeeze()
        # plt.imshow(img[0].transpose((1,2,0)))