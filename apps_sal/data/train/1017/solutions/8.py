for i in range(int(input())):
    a1, a2, a3, a4, a5, P = list(map(int, input().split()))
    sum = (a1 + a2 + a3 + a4 + a5) * P
    if sum > 120:
        print("Yes")
    else:
        print("No")
