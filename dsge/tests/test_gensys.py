from __future__ import division

import numpy as np
from numpy.testing import assert_equal, assert_array_almost_equal

from unittest import TestCase

#from dsge.fortran import gensysw
from dsge.DSGE import DSGE
#from dsge.gensys import gensy
import pkg_resources

class TestGensys(TestCase):

    def test_simple(self):
        RR = np.eye(3)
        TT = np.zeros((3,3))


        #TT, CC, RR, fmat, fwt, ywt, gev, RC, loose = gensysw.gensys_wrapper.call_gensys(G0, G1, C0, PSI, PPI, 1.00000000001)

        #self.assertEqual(RC,0)
        #assert_equal(np.eye(3),PP)

    def test_pc(self):
        relative_loc = ('examples/schorf_phillips_curve/'
                        'schorf_phillips_curve.yaml')
        model_file = pkg_resources.resource_filename('dsge', relative_loc)


        pc = DSGE.read(model_file)
        p0 = pc.p0()
        model = pc.compile_model()

        TT,RR,RC = model.solve_LRE(p0)

        assert_array_almost_equal(TT, np.zeros_like(TT))

        para = dict(zip(map(str,pc.parameters),p0))
        kap, tau, psi = para['kap'], para['tau'], para['psi']

        RRexact = ( (1/(1+kap*tau*psi)) *
                    np.array([[-tau, 1, -tau*psi],
                              [-kap*tau, kap, 1],
                              [1, kap*psi, psi]]))
        assert_array_almost_equal(RR[:3,:3], RRexact)

    def test_nkmp(self):

        dsge1 = DSGE.read('/home/eherbst/Dropbox/DSGE Book (1)/dsge-book/code/models/dsge1/dsge1.yaml')
        nkmp = dsge1.compile_model()

        p0 = np.array([ 1.62398783,  0.47671893,  1.51729311,  0.4416236 ,  0.43724069,
                        0.65953619,  0.60440589,  0.51634896,  5.82589805,  0.68667388,
                        0.54936489,  0.53220526,  3.20302156])

        TT = np.array([[ -1.19329721e-17,  -4.57275976e-17,  -2.36372083e-01,
                      2.26222638e-01,   3.45109676e-17,   1.10033927e-16,
                      0.00000000e+00,   0.00000000e+00,   3.46944695e-17,
                      5.55111512e-17,  -1.80411242e-16,  -2.77555756e-17],
                    [  6.29389080e-18,  -5.62321924e-17,  -1.50224229e-01,
                       1.89539159e-01,   1.12322247e-17,   1.46125509e-16,
                       0.00000000e+00,   0.00000000e+00,  -1.14491749e-16,
                       -2.08166817e-16,   2.77555756e-17,   2.08166817e-17],
                    [  1.26322487e-17,   5.90320655e-17,   2.50223574e-01,
                       2.18064570e-01,  -7.15126043e-18,   4.61608757e-17,
                       0.00000000e+00,   0.00000000e+00,  -1.71737624e-16,
                       -2.22044605e-16,   1.63064007e-16,   1.16226473e-16],
                    [ -1.61778115e-32,   5.85482703e-32,  -3.12250226e-17,
                      6.04405893e-01,  -3.08148791e-33,  -4.01992820e-17,
                      0.00000000e+00,   0.00000000e+00,  -2.28983499e-16,
                      -2.77555756e-16,  -1.38777878e-17,   4.85722573e-17],
                    [ -1.19329721e-17,  -1.79720219e-17,  -2.36372083e-01,
                      2.26222638e-01,   6.75539196e-18,   6.59536185e-01,
                      0.00000000e+00,   0.00000000e+00,  -9.02056208e-17,
                      1.52655666e-16,   2.77555756e-17,   5.55111512e-17],
                    [ -3.72653629e-33,   9.75461702e-33,   3.09885332e-17,
                      -3.51271253e-17,  -1.10534841e-32,   6.59536185e-01,
                      0.00000000e+00,   0.00000000e+00,  -6.00084073e-17,
                      4.98590071e-17,   9.61719481e-17,   0.00000000e+00],
                    [  2.38257983e-16,   1.83347506e-16,  -3.06135239e-16,
                       7.70371978e-33,   1.00000000e+00,  -3.49839765e-33,
                       0.00000000e+00,   0.00000000e+00,   3.25263527e-17,
                       3.08148791e-33,   1.72576568e-16,   8.68630112e-21],
                    [  1.94481569e-18,  -3.18498097e-17,  -2.36372083e-01,
                       8.30628531e-01,   6.75539196e-18,   6.59536185e-01,
                       0.00000000e+00,   0.00000000e+00,  -3.05311332e-16,
                       -5.55111512e-17,   0.00000000e+00,   1.11022302e-16],
                    [  1.57177714e-18,  -1.23219345e-17,  -3.75896434e-02,
                       8.18000031e-02,   1.07429258e-18,   4.12694294e-17,
                       0.00000000e+00,   0.00000000e+00,  -1.73472348e-17,
                       0.00000000e+00,  -2.42861287e-17,  -3.46944695e-18],
                    [ -9.24446373e-33,   3.54371110e-32,  -2.08166817e-17,
                      3.65306483e-01,  -1.54074396e-33,  -2.12459772e-17,
                      0.00000000e+00,   0.00000000e+00,  -1.31838984e-16,
                      -1.38777878e-16,   0.00000000e+00,   2.77555756e-17],
                    [  4.83536015e-19,  -1.48991590e-17,  -5.91458675e-02,
                       8.51859190e-02,   1.69035832e-18,   2.31527702e-16,
                       0.00000000e+00,   0.00000000e+00,  -1.04083409e-17,
                       -6.93889390e-18,  -3.12250226e-17,  -1.73472348e-17],
                    [ -2.98591094e-18,  -1.48991590e-17,  -5.91458675e-02,
                      8.51859190e-02,  -1.77908863e-18,   4.34987980e-01,
                      0.00000000e+00,   0.00000000e+00,  -5.72458747e-17,
                      3.46944695e-17,   2.42861287e-17,   2.77555756e-17]])

        RR = np.array([[  2.10029859e-16,   3.74289266e-01,  -5.40599463e-01],
                       [  7.61694535e-17,   3.13595816e-01,  -3.43573303e-01],
                       [  1.07461893e-16,   3.60791602e-01,   5.72278791e-01],
                       [ -3.33723910e-17,   1.00000000e+00,  -5.61206239e-17],
                       [  1.00000000e+00,   3.74289266e-01,  -5.40599463e-01],
                       [  1.00000000e+00,  -4.16333634e-17,  -4.77175596e-17],
                       [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
                       [  1.00000000e+00,   1.37428927e+00,  -5.40599463e-01],
                       [  5.66595299e-17,   1.35339519e-01,  -8.59701400e-02],
                       [ -2.01704698e-17,   6.04405893e-01,  -3.39196358e-17],
                       [  3.26358898e-16,   1.40941576e-01,  -1.35270730e-01],
                       [  6.59536185e-01,   1.40941576e-01,  -1.35270730e-01]])

        TT2, RR2, RC2 = nkmp.solve_LRE(p0)
        # the variables E_t[x] aren't necessarily in the same order
        nv = len(dsge1.variables)

        assert_array_almost_equal(TT2[:nv,:nv], TT[:nv,:nv])
        assert_array_almost_equal(RR2[:nv,:],RR[:nv,:])        

    # def test_single_equation(self):
    #     simple = DSGE.read('dsge/examples/simple-model/simple_model_est.yaml')
    #     p0 = simple.p0()

    #     model = simple.compile_model()
    #     print model.GAM0(p0)
    #     print model.GAM1(p0)
    #     print model.PSI(p0)
    #     print model.PPI(p0)
    #     print model.solve_LRE(p0)
    #     print fjdksalf
