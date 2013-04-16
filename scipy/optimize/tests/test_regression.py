"""Regression tests for optimize.

"""
from __future__ import division, print_function, absolute_import

import numpy as np
from numpy.testing import TestCase, run_module_suite, assert_almost_equal, \
        assert_raises

import scipy.optimize

class TestRegression(TestCase):

    def test_newton_x0_is_0(self):
        """Ticket #1074"""

        tgt = 1
        res = scipy.optimize.newton(lambda x: x - 1, 0)
        assert_almost_equal(res, tgt)

    def test_newton_integers(self):
        """Ticket #1214"""
        root = scipy.optimize.newton(lambda x: x**2 - 1, x0=2,
                                    fprime=lambda x: 2*x)
        assert_almost_equal(root, 1.0)

    def test_lmdif_errmsg(self):
        # this shouldn't cause a crash on Python 3
        class SomeError(Exception):
            pass
        counter = [0]
        def func(x):
            counter[0] += 1
            if counter[0] < 3:
                return x**2 - np.array([9, 10, 11])
            else:
                raise SomeError()
        assert_raises(SomeError,
                      scipy.optimize.leastsq,
                      func, [1, 2, 3])

if __name__ == "__main__":
    run_module_suite()
