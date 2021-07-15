t=int(input())
for i in range(t):
    n=input().strip()
    sev=n.count('7')
    four=n.count('4')
    print(len(n)-(sev+four))
    

