import numpy as np
from ase.phonons import Phonons
from phonopy import Phonopy
from phonopy.structure.atoms import PhonopyAtoms

from ase import Atoms
from ase.io import read, write

import numpy

import os
import shutil

from phonopy.interface.calculator import read_crystal_structure, write_crystal_structure

unitcell, optional_structure_info = read_crystal_structure("geometry.in", interface_mode='aims')

sup_matrix = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
det = np.round(np.linalg.det(sup_matrix))
print(np.round(det))
phonon = Phonopy(unitcell,
                 supercell_matrix=sup_matrix)

phonon.generate_displacements(distance=0.01)
supercells = phonon.supercells_with_displacements

# print(supercells[0])


crys = read("geometry.in")
print(len(crys))
charges = crys.get_initial_charges()

print(charges)

charges2 = []
print(type(charges2))
# print(charges3)

moments = crys.get_initial_magnetic_moments()
moments2 = []

for i in range(len(crys)):
    for j in range(int(det)):
        charges2.append(charges[i])
        moments2.append(moments[i])


print(len(charges2))

chem_sym = crys.get_chemical_symbols()

for ind, sup in enumerate(supercells):
    write_crystal_structure(f"geomtry_{ind}.in", supercells[ind], interface_mode='aims')
    atoms = read(f"geomtry_{ind}.in")
    atoms.set_initial_charges(charges2)
    atoms.set_initial_magnetic_moments(moments2)
    directory = f"disp_{ind}"
    parent_dir = "C:/Users/Merlin Warner-Huish/PycharmProjects/Merlin/"
    path_final = os.path.join(parent_dir, directory)
    if os.path.exists(path_final):
        shutil.rmtree(path_final)
        os.mkdir(path_final)
        atoms.write(path_final + '/geometry.in')
    else:
        os.mkdir(path_final)
        atoms.write(path_final + '/geometry.in')
    os.remove(f"geomtry_{ind}.in")

