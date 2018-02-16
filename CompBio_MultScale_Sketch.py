# Summary of Program.
# Does not take into account spec. mech.s of the packages we will end up using
# Equations taken from
# 	MICROSTRUCTURE-BASED, MULTISCALE MODELING FOR THEMECHANICAL BEHAVIOR OF HYDRATED FIBER NETWORKS∗
#	 (Chandran et. al., 2008) [ in box as Math_MultiScaleModel_Fiber.pdf]
#


import numpy as np
import random as rand
import matplotlib.pyplot as plt

def solve_FE(EqnPar1array, EqnPar2array, EqnPar3array):
	'''Solve system via FE method
	Plot Evolution of the solution
 	Plot strains '''

def macro_equation(fluid_moment, solid_moment, volume_convserv):
	''' Main equation
		Chandran et. Al. eqn 3.39 and 3.40
		?) How to write this such that our FE solver  will use take it - we will
			likely need to play the solver's game
		'''

def macro_fluid_momentum(avg_strss_Tnsr, prssre_fluc, vol_avg_regn):
	''' Takes in a calculated average stress tensor (call to function)
	 pressure fluctuation is a constant
	 Eqn:

	  -Theta^F P_J^F  = -(1/a)\int_{\Gamma = Boundary} n_i^{FS} s_{ij}^F d\Gamma
	  ( Chandran et al eqn 3.22)
			n_i^{FS} a normal vector.

	Returns the fluid portion of the macroscale equation
		NOTE:  Most integrals become sums!!
		'''


def macro_solid_momentum(avg_strss_Tnsr, prssre_fluc, vol_avg_regn):
	'''
	Eqn:

	 S_{ij}^S  = (1/a) \int_{boundary} (s_{ij}^S - S_{ij}^S)u_{k,I} n_k^a d\Gamma

	 -Theta^S P_J^S = -(1/a) \int_{boundary} n_i^{SF} (s_{ij}^S - p^S \delta_{ij} ) d\Gamma
	  (Chandran et. al. eqn 3.29)

	 Returns the solid portion of the macroscale equation
		 '''
def volume_conservation(macro_solid_veloc, vol_frac_solid, vol_frac_fluid):
	'''
		Eqn:

			(V_k^S)_K + (\Theta^F/\Theta_^S V_k^F)_k
				= (1/a) \int_{\Gamma} (V_k^S - v_k^sS)n_k^a d\Gamma

		'''

def get_avg_stress_fluid( ):
	 ''' Returns average stress tensor '''

def get_avg_stress_solid():
	'''Returns average stress tensor'''

def volume_fractions(initial_solid_vol, initial_RVE_volume):
	'''Theta^F = 1 - Theta^{S_0} (a_0/a)
			Chandran et. al. eqn 3.51
		'''

def plotter(array, array):
	''' plots stuff, may need to be pre-formatted'''

def generate_RVE():
	''' this may become its own script'''


###############################################################################

def main():
	''' stuff '''

if __name__ == "__main__"
	main()
