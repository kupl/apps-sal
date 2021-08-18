a = list(input())
b = list(input())
name = [None for _ in range(len(a))]

a.sort()
b.sort(reverse=True)


ai = 0
aj = (len(a) + 1) // 2 - 1
bi = 0
bj = len(b) // 2 - 1

turn = 0
ansi = 0
ansj = len(name) - 1
for _ in range(len(name)):
    if not turn:

        if a[ai] < b[bi]:
            name[ansi] = a[ai]
            ai += 1
            ansi += 1

        else:
            name[ansj] = a[aj]
            aj -= 1
            ansj -= 1

    else:

        if b[bi] > a[ai]:
            name[ansi] = b[bi]
            bi += 1
            ansi += 1

        else:
            name[ansj] = b[bj]
            bj -= 1
            ansj -= 1

    turn ^= 1

print(''.join(name))
