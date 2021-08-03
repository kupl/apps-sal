def chef(a):
    b = []
    c = 0
    b = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]
    for i in range(len(a)):
        if ord(a[i]) in b:
            continue
        else:
            c += int(chef2(a[i], b))
    return c


def chef2(a, b):
    c = []
    for i in b:
        c.append(abs(ord(a) - i))
    return min(c)


T = int(input())
for _ in range(T):
    a = input()
    print(chef(a))
