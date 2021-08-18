for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    k = int(input())
    for j in range(k):
        s, e = list(map(int, input().split()))
        su = sum(arr[s - 1:e])
        print(su)
