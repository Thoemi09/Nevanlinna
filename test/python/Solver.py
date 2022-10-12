#!/usr/bin/env python

import unittest

from nevanlinna import Solver
from h5 import *
from triqs.gf import GfImFreq, GfReFreq, MeshReFreq, iOmega_n, Omega, inverse

class test_solver(unittest.TestCase):

    def test_solver(self):
        eta = 0.1
        m = MeshReFreq(-5.0, 5.0, 101)
        g_im = GfImFreq(indices = [1], beta = 50, n_points = 1000, name = "$G_\mathrm{imp}$")
        g_re = GfReFreq(indices = [1], mesh = m)
        g_im << inverse(iOmega_n + 0.5)
        g_re << inverse(Omega + eta*1.j + 0.5)
        solver = Solver()
        solver.solve(g_im)
        g_re_solver = solver.evaluate(m, eta)
        pass


if __name__ == '__main__':
    unittest.main()
