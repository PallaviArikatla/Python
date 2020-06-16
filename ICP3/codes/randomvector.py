import numpy as np
x = np.random.random(20)
print("Original array:")
print(x)
reshapearray=x.reshape((4,5))
print(reshapearray)
c = np.where(reshapearray==np.amax(reshapearray,axis=1,keepdims=True),0,reshapearray)
print(c)