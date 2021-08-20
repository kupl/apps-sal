from sys import stdin, stdout
t = int(stdin.readline())
while t:
    t -= 1
    m = int(stdin.readline())
    n = int(stdin.readline())
    o = int(stdin.readline())
    if m > 2 and n > 2 and (o > 2):
        ans = 4 * (m + n + o - 6)
    elif m == 1 or n == 1 or o == 1 or (m == 2 and n == 2 and (o == 2)):
        ans = 0
    else:
        ans = m - 2 if m > 2 else 0
        ans += n - 2 if m > 2 else 0
        ans += o - 2 if m > 2 else 0
    stdout.write(str(ans) + '\n')
