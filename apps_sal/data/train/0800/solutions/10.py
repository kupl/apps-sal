T = int(input())
s = input() + ' '
n = 0
maxn = 0
for i in range(T):
    term = ''
    y = s[n]
    while y != ' ':
        term += y
        n += 1
        y = s[n]
    n += 1
    if int(term) > maxn:
        maxn = int(term)
    if i == 0:
        minn = int(term)
    elif int(term) < minn:
        minn = int(term)
print(maxn, minn)
