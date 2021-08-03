N = int(input())
for i in range(N):
    a = int(input())
    li = [int(x) for x in input().split()]
    a = min(li)
    print(a * (len(li) - 1))
