from __future__ import print_function
import numpy
from numpy import triu, tril
x = numpy.random.rand(3, 3, 3, 3)

y = triu(x, k=0, axes=(0,1))
assert tril(y[:, :, 0, 0], k=-1).sum() == 0.0

z = tril(x, k=0, axes=(0,1))
assert triu(z[:, :, 0, 0], k=1).sum() == 0.0

print('done')
