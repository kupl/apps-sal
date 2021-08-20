t = int(input())
for _ in range(t):
    a = input()
    for i in range(len(a) - 1, -1, -1):
        print(a[i], end='')
    print()
