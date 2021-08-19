"""input
aaaaaaaaaa
"""


def lexi_sum(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    t = 0
    for l in s:
        t += a.index(l) + 1
    return t


def shift(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    s1 = ''
    for l in s:
        s1 += a[a.index(l) - 1]
    return s1


s = input()
if set(s) == set('a'):
    print(s[:-1] + 'z')
    quit()
s = s.split('a')
m = s[0]
k = 1
while len(m) < 1:
    m = s[k]
    k += 1
m1 = s.index(m)
s[m1] = shift(m)
print('a'.join(s))
