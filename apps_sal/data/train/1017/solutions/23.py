T = int(input())
for i in range(T):
    A1, A2, A3, A4, A5, P = list(map(int, input().split()))
    sum = (A1 + A2 + A3 + A4 + A5) * P
    if sum > 120:
        print("Yes")
    else:
        print("No")
