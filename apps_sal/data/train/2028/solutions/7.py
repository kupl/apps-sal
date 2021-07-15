s = input()
n = len(s)

if n <= 2:
    print('Impossible')
    return

if len(s) % 2 == 1:
    s = s[:n//2] + s[n//2 + 1:]
    if len(set(s)) == 1:
        print('Impossible')
        return
    print(2)
    return

if len(set(s)) == 1:
    print('Impossible')
    return

for i in range(0, n):
    cut = s[:i]
    orig = s[i:]
    pal = orig + cut
    if pal == pal[::-1] and pal != s:
        print(1)
        return

print(2)
return

