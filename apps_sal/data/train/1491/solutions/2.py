(a, b, c, d) = list(map(int, input().split()))
if a * b == c * d or a * c == b * d or a * d == b * c:
    print('Possible')
else:
    print('Impossible')
