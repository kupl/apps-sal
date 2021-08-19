# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 2:
        l = list(range(1, n))
    else:
        l = list(range(1, n + 1))
    for i in range(0, len(l), 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    if n % 2:
        l.append(n)
        l[n - 2], l[n - 1] = l[n - 1], l[n - 2]
    for i in l:
        print(i, end=" ")
    print()
