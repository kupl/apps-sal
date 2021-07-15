seq = int(input())
while seq>0:
    level = [0]*101
    n,m = input().split()
    m = int(m)
    n = int(n)
    power =0
    while n>0:
        c,l = input().split()
        c = int(c)
        l = int(l)
        level[l] = level[l] + c
        n = n -1;
    while m>0:
        c,l = input().split()
        c = int(c)
        l = int(l)
        level[l] = level[l] - c
        m = m -1;
    for no in level:
        if no<0:
            power = power + (-no)
    print(power)	
    seq =seq - 1

