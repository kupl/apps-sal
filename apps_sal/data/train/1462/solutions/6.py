try:
    for t in range(int(input())):
        inp = input().lower()
        b = False
        s = False
        for i in inp.split():
            if i == 'berhampore':
                b = True
            elif i == 'serampore':
                s = True
        if b and s:
            print('Both')
        elif b:
            print('GCETTB')
        elif s:
            print('GCETTS')
        else:
            print('Others')
except:
    pass
