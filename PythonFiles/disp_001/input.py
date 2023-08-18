from ase import Atoms
from ase.calculators.aims import Aims
from ase.optimize import BFGS
from ase.io import read, write
from ase.io.trajectory import Trajectory
from ase.constraints import ExpCellFilter

#New method:
from carmm.run.aims_path import set_aims_command
set_aims_command(hpc="isambard", basis_set="light", defaults=2020)

# Build molecule
crys = read('geometry.in')

# New method that gives a default calculator
from carmm.run.aims_calculator import get_aims_calculator
fhi_calc = get_aims_calculator(dimensions=3)

from carmm.run.aims_calculator import get_k_grid
k_grid = get_k_grid(crys, sampling_density=0.0534)

#k_grid = (1,1,1)

# Change some FHI-aims calculation settings
fhi_calc.set(
         spin='none',
         compute_forces=True,
         compute_analytical_stress=True,
         k_grid=k_grid,
         relativistic=('atomic_zora','scalar'),
         sc_accuracy_etot=1e-6,
         sc_accuracy_eev=1e-3,
         sc_accuracy_rho=1e-6,
         sc_accuracy_forces=1e-4,
        )


crys.set_calculator(fhi_calc)

energy = crys.get_potential_energy()

print(f" Total energy: {crys.get_potential_energy()}")
print(f" Cell Volume: {crys.get_volume()}")
print(f" Cell parameters: {crys.get_cell_lengths_and_angles()}")
    

