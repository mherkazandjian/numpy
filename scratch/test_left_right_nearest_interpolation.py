import numpy
from numpy import int
import pylab

x = numpy.linspace(0, 10, 100)
y = numpy.sin(x)

xi = numpy.linspace(0, 10, 10000)
# xi = numpy.array([0.0, 0.33, 0.5, 0.73, 4.0])

pylab.plot(x, y, 'o')

def nearest_left_neigbour_interpolate(xi, x, y):
    """

    :param x:
    :param xp:
    :param yp:
    :return:
    """
    inds_matching_exactly = numpy.where(numpy.in1d(x, xi))
    inds_not_matching_exactly = numpy.where(~numpy.in1d(xi, x))

    assert inds_matching_exactly[0].size + inds_not_matching_exactly[0].size == xi.size

    x_matching = x[inds_matching_exactly]
    y_matching = y[inds_matching_exactly]


    x_not_matching = xi[inds_not_matching_exactly]
    y_not_matching = y[numpy.searchsorted(x, xi[inds_not_matching_exactly]) - 1]

    xi_new = numpy.hstack([x_matching, x_not_matching])
    inds_sort = numpy.argsort(xi_new)
    xi_new = xi_new[inds_sort]
    yi_new = numpy.hstack([y_matching, y_not_matching])
    yi_new = yi_new[inds_sort]

    return yi_new


pylab.plot(xi, nearest_left_neigbour_interpolate(xi, x, y), '-')

pylab.xlim([-1, 7])
pylab.ylim([-1.2, 1.2])

pylab.show()


print('done')

