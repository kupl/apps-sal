s = input()
cnt = 0
m = 10**9 + 7
t = 0

for i in range(len(s)):
    if s[~i] == 'a':
        cnt = (cnt + t) % m
        t = (t * 2) % m
    else:
        t += 1
print(cnt)

"""s = raw_input()
m = 0
n = 0
twop = 1
ans = 0
mold = [0,0]
isbool1 = True
isbool2 = False

def twopower(x):
    d = {0:1}
    if x in d:
        return d[x]
    else:
        if x%2 == 0:
            d[x] = twopower(x/2)**2
            return d[x]
        else:
            d[x] = twopower(x-1)*2
            return d[x]

for char in s:
    if char == "a":
        m += 1
    else:
        ans += twopower(m)-1
        ans = ans%(10**9+7)

print ans%(10**9+7)"""

"""
for char in s:
    if char == "a":
        m += 1
        if isbool == True:
            twop *= twopower(m-mold[1])
            ans += n*(twop-1)
            isbool = False
            n = 0
    else:
        mold = [mold[1],m]
        n += 1
        isbool = True

if s[-1] == "a":
    print ans
else:
    twop *= twopower(m-mold[0])
    ans += n*(twop-1)
    print ans
"""
