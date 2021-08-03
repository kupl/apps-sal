def abc(l):
    for i in l:
        if i == 1:
            return 'Impossible'
    return 'Possible'


t = int(input())
while(t != 0):
    n = int(input())
    a = int(input())
    l = list(map(int, input().split()))
    print(abc(l))
    t -= 1
