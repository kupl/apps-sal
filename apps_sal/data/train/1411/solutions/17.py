t = int(input())
while t > 0:
    (x, r, a, b) = map(int, input().split())
    val = x * abs(a - b) // max(a, b)
    rem = x * abs(a - b) % max(a, b)
    if rem == 0:
        print(val - 1)
    else:
        print(val)
    t -= 1
