s = input()
k = input()
wrds = s.split(' ')
kl = len(k)
comp = sorted(k)


def ana(an):
    if an == k:
        return False
    return comp == sorted(an)


ans = ''
for x in range(0, len(wrds)):
    word = wrds[x]
    if len(word) == kl and ana(word):
        ans += str(x + 1)
print('The antidote is found in %s.' % ans)
