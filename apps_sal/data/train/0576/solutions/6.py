n = int(input())
for _ in range(n):
    c = 0
    s = input()
    for i in s:
        if i == 'a':
            c += 1
    print(2 ** len(s) - 2 ** (len(s) - c))
