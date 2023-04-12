Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> setup='''
import numpy as np
L=range(100)
a=np.arange(100)
'''
>>> import timeit
>>> timeit.timeit("[i**2 for i in L]", setup)
17.235830599999986
>>> setupL='''
import numpy as np
a=np.arange(10000)
'''
>>> timeit.timeit("[a+1]", setupL,number =100)
0.0008415000000354667
>>> timeit.timeit("[a**2]", setupL,number =100000)
0.6160376000000269
>>> timeit.timeit("[a**2]", setupL)
6.0985847000000035
>>> timeit.timeit("[a+2]", setupL)
4.598539000000017
>>> 