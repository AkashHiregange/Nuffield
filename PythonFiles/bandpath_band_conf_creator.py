from ase.build import bulk

atoms = bulk('Al', 'fcc', a=4.05)

lat1 = atoms.cell.bandpath()
band_label = []
band = []
for sp in lat1.path:
    if sp == 'G':
        band_label.append('$\Gamma$')
    elif sp.isnumeric():
        band_label[-1] = band_label[-1]+sp
    else:
        band_label.append(sp)
for sp in band_label:
    if sp !=',':
        if sp == '$\Gamma$':
            band.append('0 0 0')
        else:
            cor1 = lat1.special_points[sp][0]
            cor2 = lat1.special_points[sp][1]
            cor3 = lat1.special_points[sp][2]
            band.append(f'{cor1} {cor2} {cor3}')
    elif sp == ',':
        band[-1]=band[-1]+','

for i in band_label:
    if i == ',':
        band_label.pop(band_label.index(i))

        
band_label_final = ' '.join(band_label)
print(band_label_final)
band_final = '    '.join(band)
print(band_final)

try:
    f = open('band.conf', 'x')
    f.close()
except:
    print()

f = open('band.conf', 'w')
f.write(f'BAND = {band_final}\n'
        f'BAND_LABELS = {band_label_final}\n'
        f'BAND_POINTS = 101')
