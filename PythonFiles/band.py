from ase.build import bulk
import ase

si = bulk('Si', 'diamond', a=5.459)
lat = si.cell.get_bravais_lattice()
print(list(lat.get_special_points()))

print(ase.lattice.BravaisLattice.bandpath(lat))