import numpy as np
import statistics as stat

scores=np.array([2, 3, 4, 5, 0, 1, 3, 3, 4, 3])
n=len(scores)
mean=sum(scores)/n
print(mean)

median=stat.median(scores)
print(median)

mode=stat.mode(scores)
print(mode)


