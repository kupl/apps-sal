s = input()
cnt = 0
m = 10 ** 9 + 7
t = 0
for i in range(len(s)):
    if s[~i] == 'a':
        cnt = (cnt + t) % m
        t = t * 2 % m
    else:
        t += 1
print(cnt)
's = raw_input()\nm = 0\nn = 0\ntwop = 1\nans = 0\nmold = [0,0]\nisbool1 = True\nisbool2 = False\n\ndef twopower(x):\n    d = {0:1}\n    if x in d:\n        return d[x]\n    else:\n        if x%2 == 0:\n            d[x] = twopower(x/2)**2\n            return d[x]\n        else:\n            d[x] = twopower(x-1)*2\n            return d[x]\n\nfor char in s:\n    if char == "a":\n        m += 1\n    else:\n        ans += twopower(m)-1\n        ans = ans%(10**9+7)\n\nprint ans%(10**9+7)'
'\nfor char in s:\n    if char == "a":\n        m += 1\n        if isbool == True:\n            twop *= twopower(m-mold[1])\n            ans += n*(twop-1)\n            isbool = False\n            n = 0\n    else:\n        mold = [mold[1],m]\n        n += 1\n        isbool = True\n\nif s[-1] == "a":\n    print ans\nelse:\n    twop *= twopower(m-mold[0])\n    ans += n*(twop-1)\n    print ans\n'
