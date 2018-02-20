"""
    Solves
    (weak form of eqn 12, Chandran and Barocas)
    \[    \ nabla S_{ij} - (1/a) (s_{ij}-S_{ij})u_{k,I} = 0    \]
    *TODO* check this Equation

    Look at examples on
    http://sfepy.org/doc-devel/examples.html
    Table of terms for PDEs
    http://sfepy.org/doc-devel/term_table.html?highlight=dw_surface_ltr

    EDITED: 2/5/18 (dean k) adapted this example:
    http://sfepy.org/doc-devel/examples/large_deformation/active_fibres.html
    to our problem. Still have many quesitons.

    EDITED: 2/16/18 (rachel) fixed syntax errors so that code will run

    EDITED: 2/20/18 (dean) edited equation definition
    """

import numpy as np
from sfepy import data_dir

filename_mesh = data_dir + '/meshes/2d/' #TODO determine which mesh

vf_matrix = 1.0
# If we add fibers
#vf_fibres1 = some number
#vf_fibres2 = some number2

options = {
    'nls' : 'newton',
    'ls' : 'ls',
    'ts' : 'ts',
    'save_steps' : -1,
    'post_process_hook' : 'stress_strain',
}

fields = {
    'displacement':(np.float64, 2, 'Omega',1),  # The 2 refers to dof.
}

materials = {
    'solid' : ({
               'K'  : vf_matrix * 1e3, # bulk modulus
               'mu' : vf_matrix * 20e0, # shear modulus of neoHookean term
               },),
#'f1' : 'get_pars_fibres1',
#'f2' : 'get_pars_fibres2',
}

variables = {
    'u' : ('unknown field', 'displacement', 0),
    'v' : ('test field', 'displacement', 'u'),
}

regions = {
    'Omega' : 'all',
    'Left' : ('vertices in (x < 0.001)', 'facet'),
    'Right' : ('vertices in (x > 0.099)', 'facet'),
}

# Dirichlet BC.
ebcs = {
    'l' : ('Left', {'u.all' : 0.0}),
}

# define an integral of order 1
integral_1 = {
    'name' : 'i',
    'order' : 1,
}

#balance equations
# TODO check check check these!
# CURRENTLY, set s_{ij} = 0 for all i,j representing the fact that the microscale
# momentum is not being considered. The equation  then is
#\[ \ nabla S = (1/a) int_surf ( - nabla S ) \cdot n dI
# Set Volume, a =  1 for now as well.

equations = {
    'balance'
        : """ ev_surface_div.i.Left(v, u) + ev_surface_div.i.Right(v, u) + ev_surface_integrate.i.Left(solid.mu, v, u)
                + ev_surface_integrate.i.Right(solid.mu, v, u)


                = 0""",
        # : """dw_tl_he_neohook.i.Omega( solid.mu, v, u )
        #     + dw_tl_bulk_penalty.i.Omega( solid.K, v, u )
        #
        #     = 0""",
}

# Where the calc is going to be done.
# TODO prettttttty sure this is wrong for our problem or at least are very un polished
#   i.e., See Chandran, Barocas Eqn 12
def stress_strain(out, problem, state, extend=False):
    from sfepy.base.base import Struct, debug

    ev = problem.evaluate
    # call the equation term 'dw_tl_he_nehook', the integral 'i', the region for
    #   for integration 'Omega', then call the materials, the test fcn and unknown fcn
    #TODO Does this work - plugging in this sum of terms?
    strain = ev('ev_surface_div.i.Left(v, u) + ev_surface_div.i.Right(v, u)+ ev_surface_integrate.i.Left(solid.mu, v, u) + ev_surface_integrate.i.Right(solid.mu, v, u)',
                mode='el_avg', term_mode='strain')
    out['green_strain'] = Struct(name='output_data', mode='cell', data=strain, dofs=None)

     stress = ev('ev_surface_div.i.Left(v, u) + ev_surface_div.i.Right(v, u)+ ev_surface_integrate.i.Left(solid.mu, v, u) + ev_surface_integrate.i.Right(solid.mu, v, u)',
     mode='el_avg', term_mode='stress')
     out['stress'] = Struct(name='output_data',mode='cell', data=stress, dofs=None )

    # stress = ev('dw_tl_bulk_penalty.i.Omega( solid.K, v, u )', mode='el_avg', term_mode= 'stress')
    # out['bulk_stress'] = Struct(name='output_data',mode='cell', data=stress, dofs=None)
    # List of the 3 terms
    return out

solver_0 = {'name' : 'ls',
            'kind' : 'ls.scipy_direct',
}

# Workhorses.
solver_1 = {
    'name' : 'newton',
    'kind' : 'nls.newton',

    'i_max'      : 7,  # iterations? See page 140 in 2D_collagen_gel
    #   (may set to 1 and bounce between this solver and the microscale problem)
    'eps_a'      : 1e-10,
    'eps_r'      : 1.0,
    'macheps'    : 1e-16,
    'lin_red'    : 1e-2, # Linear system error < (eps_a * lin_red).
    'ls_red'     : 0.1,
    'ls_red_warp': 0.001,
    'ls_on'      : 1.1,
    'ls_min'     : 1e-5,
    'check'      : 0,
    'delta'      : 1e-6,
}

solver_2 = {
    'name' : 'ts',
    'kind' : 'ts.simple',

    't0'    : 0,
    't1'    : 1,
    'dt'    : None,
    'n_step' : 21, # has precedence over dt!
}

def main():
#TODO Finish main (/ start main)
    print "Finish main (/start main)"
    return

if __name__  == "__main__":
    main()
