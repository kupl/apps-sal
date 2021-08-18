for i in range(eval(input())):
    n, m, z, l, r, b = list(map(int, input().split()))
    rows = n
    columns = m
    hand_rest = n * (m + 1)
    if(m % 2 == 0):
        hand_rest -= max(0, n - l - r)
    if(l + r + (2 * b) <= hand_rest):
        print(min(n * m, l + r + z + b))
    else:
        temp = l + r + (hand_rest - l - r) / 2
        print(min(n * m, temp + z))
