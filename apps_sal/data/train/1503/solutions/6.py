def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


for _ in range(int(input())):
    (m, n) = map(int, input().split())
    hcf = compute_hcf(m, n)
    print(m // hcf * n // hcf)
