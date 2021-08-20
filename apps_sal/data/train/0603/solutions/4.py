l = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy\xa0\xa0\xa0\xa0zabcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    n = int(input())
    x = n // 25
    if n % 25 == 0:
        x = x - 1
    x = n + 1 + x
    s = l[:x]
    print(s[::-1])
