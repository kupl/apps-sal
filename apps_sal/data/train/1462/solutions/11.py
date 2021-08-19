t = int(input())
c = 0
d = 0
for i in range(t):
    c = 0
    d = 0
    s = input()
    l = s.split(' ')
    for j in range(len(l)):
        if l[j].lower() == 'berhampore':
            c += 1
        if l[j].lower() == 'serampore':
            d += 1
    if c > 0 and d > 0:
        print('Both')
    elif c > 0:
        print('GCETTB')
    elif d > 0:
        print('GCETTS')
    else:
        print('Others')
