Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import skimage
>>> dir skimage
SyntaxError: invalid syntax
>>> dir (skimage)
['__version__', 'color', 'data', 'data_dir', 'draw', 'exposure', 'feature', 'filters', 'future', 'graph', 'io', 'measure', 'metrics', 'morphology', 'registration', 'restoration', 'segmentation', 'transform', 'util', 'viewer']
>>> import numpy as np
>>> from skimage import data
>>> import matplotlib.pyplot as plt
>>> camera =data.camera()
>>> camera
array([[200, 200, 200, ..., 189, 190, 190],
       [200, 199, 199, ..., 190, 190, 190],
       [199, 199, 199, ..., 190, 190, 190],
       ...,
       [ 25,  25,  27, ..., 139, 122, 147],
       [ 25,  25,  26, ..., 158, 141, 168],
       [ 25,  25,  27, ..., 151, 152, 149]], dtype=uint8)
>>> chelsea =data.chelsea()
>>> chelsea
array([[[143, 120, 104],
        [143, 120, 104],
        [141, 118, 102],
        ...,
        [ 45,  27,  13],
        [ 45,  27,  13],
        [ 45,  27,  13]],

       [[146, 123, 107],
        [145, 122, 106],
        [143, 120, 104],
        ...,
        [ 46,  29,  13],
        [ 45,  29,  13],
        [ 47,  30,  14]],

       [[148, 126, 112],
        [147, 125, 111],
        [146, 122, 109],
        ...,
        [ 48,  28,  17],
        [ 49,  29,  18],
        [ 50,  30,  19]],

       ...,

       [[ 92,  58,  30],
        [105,  71,  43],
        [132,  98,  71],
        ...,
        [172, 145, 138],
        [172, 145, 138],
        [172, 145, 138]],

       [[128,  92,  60],
        [139, 103,  71],
        [134,  95,  64],
        ...,
        [166, 142, 132],
        [166, 142, 132],
        [167, 143, 133]],

       [[139, 103,  71],
        [127,  88,  57],
        [125,  86,  53],
        ...,
        [161, 137, 127],
        [161, 137, 127],
        [162, 138, 128]]], dtype=uint8)
>>> chelsea.dtype
dtype('uint8')
>>> chelsea.shape
(300, 451, 3)
>>> plt.imshow(chelsea)
<matplotlib.image.AxesImage object at 0x000001951DE30CA0>
>>> plt.show
<function show at 0x000001951B65E940>
>>> plt.show()
>>> from skimage import filters
>>> filter_chelsea = filters.gaussian(chelsea,5)

Warning (from warnings module):
  File "C:\HI_Course\python_file\lib\site-packages\skimage\_shared\utils.py", line 348
    return func(*args, **kwargs)
RuntimeWarning: Images with dimensions (M, N, 3) are interpreted as 2D+RGB by default. Use `multichannel=False` to interpret as 3D image with last dimension of length 3.
>>> filtered_images=filters.gaussian(camera,5)
>>> plt.imshow(filtered_images)
<matplotlib.image.AxesImage object at 0x000001951CFC4B50>
>>> plt.show()
>>> 