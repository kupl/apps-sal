for _ in range(int(input())):
    num = list(map(int, input().split()))
    A, B, C = sorted(num)
    if(A >= 1 and B >= 1 and C >= 1):
        if(A**2 + B**2) == C**2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
