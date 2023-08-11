from ase import Atoms

atoms = Atoms('N3', [(0, 0, 0), (1, 0, 0), (0, 0, 1)])
atoms.positions *= 2
atoms.positions[1] = (1, 1, 0)

atoms.numbers[0] = 13

#hello

atoms.symbols[2] = 'Cu'

atoms.pbc[2] = 1

atoms.cell = [2.5, 2.5, 15, 90, 90, 120]

from ase.visualize import view

#view(atoms)

from ase.io import read, write

crys = read('geometry.in')

#view(crys)

print(crys.get_initial_charges())

f = open('geometry.in', 'r')
# print(f.readlines())

lines = f.readlines()

list1 = [10, 54,3,36,346]
# print(list1[1])
string1 = 'This/is/cardiff/University'

# print(string1.split('/'))
ch_list = []
for line in lines:
    if '    initial_charge' in line:
        # pass
        charge_list = line.split()
        charge = charge_list[1]
        ch_list.append(charge)
        # print(charge)

#hi hi hi 

print(ch_list)