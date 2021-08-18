for k in range(int(input())):
    n = int(input())
    ans = "*" * (2 * n - 1)
    ar = [ans]
    l = 1
    m = 2 * n - 5
    for p in range(n - 2):
        ar.append(" " * l + "*" + " " * m + "*" + " " * l)
        l += 1
        m -= 2
    if n != 1:
        ar.append(" " * l + "*")
    ar = ar[::-1]
    for p in ar:
        print(p)
