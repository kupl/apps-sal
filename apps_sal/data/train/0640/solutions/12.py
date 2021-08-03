def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)


for i in range(int(input())):
    c = list(map(int, input().split()))
    if c[0] == c[1]:
        print(0)
    else:
        lcm = (c[0] * c[1] // hcf(c[0], c[1]))
        x = (lcm // c[0] - 1)
        y = (lcm // c[1] - 1)
        print(x + y)
