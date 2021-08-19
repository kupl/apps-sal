T = int(input())
for tc in range(T):
    # Read integers a, b and c.
    (a, b, c) = map(int, input().split(' '))
    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > a and b < c) or (b > c and b < a):
        print(b)
    else:
        print(c)
