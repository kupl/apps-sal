# cook your dish here
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    if A**2 + (B**2) == C**2:
        if A + B > C:
            print("YES")
        else:
            print("NO")
    elif B**2 + (C**2) == A**2:
        if C + B > A:
            print("YES")
        else:
            print("NO")
    elif A**2 + (C**2) == B**2:
        if A + C > B:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
