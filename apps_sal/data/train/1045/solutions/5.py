y = 10 ** 9 + 7
vo = 'aeiouAEIOU'
for _ in range(int(input())):
    s = ''.join(input().split())
    v = 0
    x = 0
    b = [1 if i not in vo else 0 for i in s[::-1]]
    for i in b:
        if i == 1:
            v += 2 ** x
        x += 1
    print(v % y)
