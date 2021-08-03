t = int(input())
T = str.maketrans('0123456789', '0101010101')
l = [0] * 300000
for _ in ' ' * t:
    a, b = input().split()
    if a == '?':
        print(l[int(b, 2)])
    else:
        l[int(b.translate(T), 2)] += 1if a == '+'else -1
