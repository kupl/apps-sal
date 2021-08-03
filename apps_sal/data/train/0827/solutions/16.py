for i in range(int(input())):
    n, k = map(int, input().split())
    l = [str(i) for i in input()]
    ac = l.count('a')
    bc = l.count('b')
    u = 0
    co = ac * bc * k * (k - 1) // 2
    for i in range(n):
        if(l[i] == 'a'):
            u = u + bc
        elif(l[i] == 'b'):
            bc = bc - 1
    co = co + u * k
    print(co)
