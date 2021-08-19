a = int(input())
for x in range(a):
    b = input()
    c = b.count('1')
    d = b.count('0')
    if c == len(b) or d == len(b):
        print(-1)
    elif len(b) & 1 == 1:
        print(-1)
    else:
        print(int(len(b) / 2) - min(c, d))
