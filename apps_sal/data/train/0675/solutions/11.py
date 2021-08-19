# cook your dish here
ml = [2**i for i in range(18)]
ml1 = [2**i + 1 for i in range(18)]

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n in ml:
        print(-1)
        continue
    l = [2, 3, 1]
    l2 = []
    i = n
    while i > 3:
        if i in ml1:
            l2 += [i - 1, i]
            i -= 1
        else:
            l2.append(i)
        i -= 1

    print(*(l + l2[::-1]))
