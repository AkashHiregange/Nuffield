#Phonon dispersion for bulk aluminum with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

#list_metals = []

atoms = bulk('Al', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
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

plt.close()

#Phonon dispersion for bulk nickle with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Ni', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.007
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Ni_phonon.png')

plt.close()

#Phonon dispersion for bulk copper with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Cu', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.005
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Cu_phonon.png')

plt.close()

#Phonon dispersion for bulk lead with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Pd', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.015
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Pd_phonon.png')

plt.close()

#Phonon dispersion for bulk silver with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Ag', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.025
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Ag_phonon.png')

plt.close()

#Phonon dispersion for bulk platinum with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Pt', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.013
bs.plot(ax=ax, emin=0.0, emax=emax)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Pt_phonon.png')

plt.close()

#Phonon dispersion for bulk gold with 7x7x7 supercell
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk('Au', 'fcc', a=4.05) #set up calc

N = 7 #phonon calc
ph = Phonons(atoms, EMT(), supercell=(N, N, N), delta=0.05)
ph.run()

ph.read(acoutsic=True) #assemble dynamic matrix
ph.clean()
path = atoms.cell.bandpath(npoints=100)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

import matplotlib.pyplot as plt #PLOT
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.015
bs.plot(ax=ax, emin=0.0, emax=0.015)
dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)
dosax.set_ylim(0, 0.015)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Au_phonon.png')