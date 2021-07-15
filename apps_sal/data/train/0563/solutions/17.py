for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for j in range(q):
        x,y = list(map(int, input().split()))
        print(sum(a[x-1:y]))

