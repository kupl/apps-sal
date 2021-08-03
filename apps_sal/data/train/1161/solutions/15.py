# cook your dish here
for h in range(int(input())):
    s = input()
    mc = s.count('m')
    l = list(s)
    k = 0
    for i in range(len(l)):
        if(l[i] == 'm'):
            if l[i - 1] == 's' and i > 0:
                l[i - 1] = '0'

            elif(i < (len(s) - 1)) and l[i + 1] == 's':
                l[i + 1] = '0'

    sc = l.count('s')

    if mc > sc:
        print('mongooses')
    elif sc > mc:
        print('snakes')
    else:
        print('tie')
