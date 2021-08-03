# cook your dish here
n = int(input())
for _ in range(n):
    m = int(input())
    lis = list(map(int, input().strip().split()))
    lis.sort()
    print(lis.index(1))
