Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/HI_Course/Sem4SoftwareEnggTechn/UI/assignment1_py_files/test_matplotlib.py
>>> plt.plot(x,y)
plt.show()
SyntaxError: multiple statements found while compiling a single statement
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001DECADE9370>]
>>> plt.show()
>>> plt.plot(x,y, 'o')
[<matplotlib.lines.Line2D object at 0x000001DEC9A31FD0>]
>>> plt.show()
>>> plt.plot(x+1,y+1, '_')
[<matplotlib.lines.Line2D object at 0x000001DEC9A774C0>]
>>> plt.show()
