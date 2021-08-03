for _ in range(int(input())):
    P1, P2, k = list(map(int, input().split()))
    d = (P1 + P2) // k
    if d % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
