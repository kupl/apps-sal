def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


for i in range(int(input())):
    (x, y) = map(int, input().split())
    print(compute_hcf(x, y))
