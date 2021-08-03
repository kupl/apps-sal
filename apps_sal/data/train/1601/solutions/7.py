t = int(input())
for test in range(t):
    n, p = map(int, input().split())
    m = round(n / 2 - 0.7)  # max possible score when i,j,k are the next integer         greater than n/2
    if m == 0:
        choices = p**3
    else:
        choices = (p - m)**2 + (p - n)**2 + (p - m) * (p - n)
    print(choices)
