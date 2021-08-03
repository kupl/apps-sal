for i in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    print(lis[0] + lis[1])
