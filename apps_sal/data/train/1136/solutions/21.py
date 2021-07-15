for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    if n%2==0:
        print((n//2)*k)
    else:
        print(((n//2)+1)*k)
