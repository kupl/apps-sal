T = int(input())
for _ in range(T):
    s = input()
    tot = 0
    for x in s:
        if 0 < ord(x) - 48 < 10:
            tot += ord(x) - 48
    print(tot)
