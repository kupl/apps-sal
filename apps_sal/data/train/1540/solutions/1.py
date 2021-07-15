for i in range(int(input())):
    n=int(input())
    k=int(input())
    if k%n==0 and k>=n:
        print("YES")
    else:
        print("NO")
