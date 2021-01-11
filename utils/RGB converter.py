from PIL import Image as imgg
import imageio
from matplotlib import pyplot as plt
import io
from csbdeep.utils import download_and_extract_zip_file, plot_some, axes_dict
from tifffile import imread
import numpy as np

# download_and_extract_zip_file (
#     url       = 'http://csbdeep.bioimagecomputing.com/example_data/retina.zip',
#     targetdir = 'data',
# )
# im = imread('data/retina/nGFP_0.1_0.2_0.5_20_31_mid-late.tif')
imge = imageio.mimread('data/EXP280_Smed_live_RedDot1_slide_mnt_N3_stk3.tif',memtest="500MB")[12]
# imge = imgg.open("data/frames1-20_input_n_avg_10_all.tif")
# imge.show()
# imge.save("converted.png")
# for i in range(5):
    # fig = plt.figure(frameon=False)
    # fig.set_size_inches(im.shape[2]/100, im.shape[3]/100)
    # ax = plt.Axes(fig, [0., 0., 1., 1.])
    # ax.set_axis_off()
    # fig.add_axes(ax)
    # ax.imshow(im[i][0], aspect='auto')
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # imge = imgg.open(buf).convert('RGB')
    # imge.save("data/converted.png")
    # buf.close()
fig = plt.figure(frameon=False)
fig.set_size_inches(imge.shape[1]/100,imge.shape[0]/100)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(imge, aspect='auto')
buf = io.BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
imge = imgg.open(buf)
imge.save("data/converted.png")
buf.close()