test = int(input())
for _ in range(test):
    n = input()
    i = t = 0
    l = len(n)
    if l == 0:
        continue
    j = l - 1
    while i < l // 2:
        if n[i] != n[j]:
            t = 1
            break
        i += 1
        j -= 1
    if t == 0:
        print(1)
    else:
        print(2)
