t = int(input())
while t:
    n1, n2, m = [int(x) for x in input().split()]
    if n2 < n1:
        temp = n1
        n1 = n2
        n2 = temp
    sum_m = m * (m + 1) / 2
    if sum_m >= n1:
        print(n2 - n1)
    else:
        print(n1 + n2 - 2 * sum_m)
    t -= 1
