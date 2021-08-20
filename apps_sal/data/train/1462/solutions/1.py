tc = int(input())
for i in range(tc):
    cllg = input()
    cllg = cllg.lower()
    cllglist = cllg.split()
    if 'berhampore' in cllglist and 'serampore' in cllglist:
        print('Both')
    elif 'berhampore' in cllglist:
        print('GCETTB')
    elif 'serampore' in cllglist:
        print('GCETTS')
    else:
        print('Others')
