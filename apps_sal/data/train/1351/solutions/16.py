T = int(input())
for i in range(T):
    N = int(input())
    l1 = [int(i) for i in input().split()]
    for i in range(N):
        if i in l1:
            print(i, end=' ')
        else:
            print(0, end=' ')
    else:
        print()
