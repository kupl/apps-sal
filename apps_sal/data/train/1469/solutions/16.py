def fk(s: str):
    s = int(s)
    for i in range(2, 1 + 1 + int(s)):
        for k in range(i, i + s):
            print(k, end='')
        print()


n = input()
n = int(n)
t = [fk(input()) for i in range(n)]
