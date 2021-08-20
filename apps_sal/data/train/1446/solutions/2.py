s = set()
for i in range(31):
    s.add(2 ** i - 1)
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
    elif n in s:
        print(n // 2)
    else:
        print(-1)
