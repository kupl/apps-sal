t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    a.pop()
    b.sort()
    b.pop()
    al = sum(a)
    bob = sum(b)
    if(al < bob):
        print('Alice')
    elif(al == bob):
        print('Draw')
    else:
        print('Bob')
    t = t - 1
