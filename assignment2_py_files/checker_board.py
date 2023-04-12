
import numpy as np
check = np.zeros((8,8))
check
check[::2, 1::2] = 1
check
check[1::2, ::2] = 1
check
import matplotlib.pyplot as plt
plt.imshow(check, cmap='Blues', interpolation='nearest')
plt.show()






