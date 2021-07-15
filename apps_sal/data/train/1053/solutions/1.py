for x in range(int(input())):
    n = int(input())
    S = list(map(int,input().split()))
    ind = n - sum(S)
    print(ind)
