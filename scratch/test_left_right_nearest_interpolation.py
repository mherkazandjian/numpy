import numpy
from numpy import int
import pylab

# x = numpy.linspace(0, 10, 21)
x = numpy.linspace(0, 10, 100)
y = numpy.sin(x) + 0.1

xi = numpy.linspace(0, 10, 10000)
# xi = numpy.array([0.0, 0.33, 0.5, 0.73, 4.0])

pylab.plot(x, y, 'o')

def nearest_left_neigbour_interpolate(xi, x, y):
    """

    :param xi: the values where the interpolation will be done
    :param x: The x values of the data points (i think they must be in
     increasing order [not sure though])
    :param y: The y values of the data points corresponding to x
    :return: The interpolated y values
    """

    yi = numpy.zeros(xi.size, 'f8')

    inds_not_matching_exactly = numpy.where(~numpy.in1d(xi, x))

    # assert inds_matching_exactly[0].size + inds_not_matching_exactly[0].size == xi.size

    yi[numpy.where(numpy.in1d(xi, x))] = y[numpy.where(numpy.in1d(x, xi))]
    yi[inds_not_matching_exactly] = y[numpy.searchsorted(x, xi[inds_not_matching_exactly]) - 1]

    return yi

pylab.plot(xi, nearest_left_neigbour_interpolate(xi, x, y), '-')

pylab.xlim([-1, 7])
pylab.ylim([-1.2, 1.2])

pylab.show()


print('done')

