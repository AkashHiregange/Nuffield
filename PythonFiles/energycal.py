#BASIC CALCULATIONS
from ase import Atoms
from ase.calculators.emt import EMT

atom = Atoms('N')
atom.calc = EMT()
e_atom = atom.get_potential_energy()

d = 1.1
molecule = Atoms('2N', [(0., 0., 0.), (0., 0., d)])
molecule.calc = EMT()
e_molecule = molecule.get_potential_energy()

e_atomization = e_molecule - 2 * e_atom

print("N atom energy: " + str(e_atom) + "eV")
print("N molecule energy: " + str(e_molecule) + "eV")
print("Atomisation energy: " + str(-e_atomization) + "eV")


#Phonon dispersion for bulk aluminum with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Al', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath('GXULGK', npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.035
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Al_phonon.png')
