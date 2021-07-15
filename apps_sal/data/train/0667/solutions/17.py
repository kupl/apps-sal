# cook your dish here
t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    days = list(map(int, input().split()))
    x = d
    for i in range(n-1, -1, -1):
        x = x // days[i] * days[i]
    print(x)     
            

            
            

