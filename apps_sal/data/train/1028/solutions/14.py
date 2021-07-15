tc=int(input())
for i in range(tc):
    n=int(input())
    m=str(n)
    length=len(m)
    m=[int(i) for i in m]
    sum=0
    for j in m:
        sum+=j**length
    
    if sum==n:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
