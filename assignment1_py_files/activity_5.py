Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([[1,2,3],[4,5,6]])
>>> a.reshape((3,2))
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> b=np.transpose(a)
>>> b
array([[1, 4],
       [2, 5],
       [3, 6]])
>>> a.mean
<built-in method mean of numpy.ndarray object at 0x000001836F67D990>
>>> a.mean()
3.5
>>> np.std(a)
1.707825127659933
>>> np.median(a)
3.5
>>> 