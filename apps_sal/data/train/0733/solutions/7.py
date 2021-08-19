t = int(input())
for i in range(t):
    l = int(input())
    st = input()
    if st == '':
        print('')
    else:
        minC = st[0]
        for s in st:
            if s < minC:
                minC = s
        print(minC)
