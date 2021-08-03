# cook your dish here
cases = int(input())
for case in range(cases):
    N = int(input())
    count = 0
    for _ in range(N):
        S, J = list(map(int, input().split()))
        if abs(J - S) > 5:
            count += 1
    print(count)
