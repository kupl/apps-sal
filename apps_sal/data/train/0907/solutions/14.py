for _ in range(int(input())):
    n = int(input())
    s = input()
    flag = 0
    m = '0'
    l = list(s)
    for i in s:
        if(i == '.'):
            l.remove(i)
    k = len(l)
    if(k == 0):
        print("Valid")
    else:
        for i in range(0, k):
            if(l[0] == 'T'):
                flag = 1
                break
            if((l[i] == 'H' and m == 'H') or (l[i] == 'T' and m == 'T')):
                flag = 1
                break
            if(l[i] == 'H'):
                m = 'H'
            if(l[i] == 'T'):
                m = 'T'
        if(flag == 0 and l[k - 1] == 'T'):
            print('Valid')
        else:
            print('Invalid')
