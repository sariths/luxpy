# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:06:06 2017

@author: kevin.smet
"""

import luxpy as lx
import numpy as np


spd = np.vstack((lx._cie_illuminants['D65'],lx._cie_illuminants['A'][1],lx._cie_illuminants['F4'][1],lx._cie_illuminants['F5'][1]))
spd = lx._iestm30["S"]["data"]
HL17 = lx._cri_rfl["cri2012"]["HL17"]
rfl =HL17
rfl = lx._iestm30["R"]["99"]["5nm"]
xyz1 = lx.spd_to_xyz(spd,rfl=rfl,cieobs = "1931_2",relative=True)
xyz2 = lx.spd_to_xyz(spd)
D65=lx._cie_illuminants['D65']
E=lx._cie_illuminants['E']
