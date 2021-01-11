import numpy as np
import matplotlib.pyplot as plt
from tifffile import imread
from tifffile import imwrite
from csbdeep.utils import download_and_extract_zip_file, plot_some, axes_dict
from csbdeep.io import save_training_data
from csbdeep.data import RawData, create_patches
from csbdeep.data.transform import anisotropic_distortions
from PIL import Image as im
from PIL import ImageOps
import io


x = plt.imread('data\\simulator_data\\converted.png')
# plt.imshow(x)
# plt.show()
# subsample = 10.2
# print('image size         =', x.shape)
# print('Z subsample factor =', subsample)
# plt.figure(figsize=(389/100, 389/100))
# plt.imshow(x, cmap='gray')
# plt.show()
# print('image size         =', x.shape)
# print('Z subsample factor =', subsample)

# raw_data = RawData.from_folder (
#     basepath    = 'data',
#     source_dirs = ['simulator_data'],
#     target_dir  = 'simulator_data',
#     axes        = 'CYX',
# )

raw_data = RawData.from_arrays(X= [x],Y= [x],axes= 'CYX')

anisotropic_transform = anisotropic_distortions (
    subsample = 1,
    psf       = np.ones((3))/9, # use the actual PSF here
    psf_axes  = 'Y',
    # poisson_noise = True,
    # gauss_sigma = 0.1
)

X, Y, XY_axes = create_patches (
    raw_data            = raw_data,
    patch_size          = (x.shape[0],x.shape[1],x.shape[2]),
    n_patches_per_image = 1,
    transforms          = [anisotropic_transform],
)
# z = axes_dict(XY_axes)['Z']
# X = np.take(X,0,axis=z)
# Y = np.take(Y,0,axis=z)
# XY_axes = XY_axes.replace('Z','')
# assert X.shape == Y.shape
# print("shape of X,Y =", X.shape)
# print("axes  of X,Y =", XY_axes)
# plt.figure(figsize=(389/100, 389/100))
for i in range(len(X)):
    fig = plt.figure(frameon=False)
    fig.set_size_inches(X[i].shape[1] / 200, X[i].shape[0] / 200)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(X[i], aspect='auto')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    imge = im.open(buf).convert('RGB')
    imge.save("data/" + str(i) + ".png")
    buf.close()
    # plt.imshow(X[i], cmap='gray')
    # plt.axis('off')
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png', bbox_inches='tight')
    # buf.seek(0)
    # imge = im.open(buf).convert('RGB')
    # imge.show()
    # imge.save("data/" + str(i) + ".png")
    # buf.close()
    # plt.show()
# for i in range(2):
#     plt.figure(figsize=(16,4))
#     sl = slice(8*i, 8*(i+1))
#     plot_some(np.moveaxis(X[sl],1,-1),np.moveaxis(Y[sl],1,-1),title_list=[np.arange(sl.start,sl.stop)])
#     plt.show()
# None;