cases=int(input())
for i in range(cases):
    n,days=map(int,input().split())
    buses=list(map(int,input().split()))
    buses.reverse()
    for j in buses:
        days=days-(days%j)
    print(days)
