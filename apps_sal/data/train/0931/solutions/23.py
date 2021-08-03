t = int(input())
while(t > 0):
    n = int(input())
    l = [int(c) for c in input().split()]
    c = 0
    for i in l:
        b = bin(i).replace('0b', '')
        if(b[-1] == '0'):
            c += i
    print(c)
    t = t - 1
