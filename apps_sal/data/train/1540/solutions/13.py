t=int(input())
for _ in range(t):
    n=int(input())
    k=int(input())
    if k<n:
        print("NO")
    else:
        if k%n==0:
            print("YES")
        else:
            print("NO")

