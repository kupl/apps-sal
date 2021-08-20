import math


def score(a):
    count = {}
    recipes = {}
    for i in range(len(a)):
        x = a[i]
        for j in range(len(x)):
            if x[j] in count:
                count[x[j]] += 1
            else:
                count[x[j]] = 1
        for ch in set(x):
            if ch in recipes:
                recipes[ch] += 1
            else:
                recipes[ch] = 1
    (num, den) = (0, 0)
    for key in recipes:
        num += math.log(recipes[key])
        den += len(a) * math.log(count[key])
    return math.exp(num - den)


t = int(input())
for _ in range(t):
    l = int(input())
    alice = []
    bob = []
    vowels = set('aeiou')
    for i in range(l):
        s = input()
        count = 2
        for j in range(len(s)):
            if s[j] in vowels:
                count += 1
            else:
                if count <= 1:
                    bob.append(s)
                    break
                count = 0
        else:
            alice.append(s)
    s1 = score(alice)
    s2 = score(bob)
    if s2 == 0 or math.exp(math.log(s1) - math.log(s2)) > 10 ** 7:
        print('Infinity')
    else:
        print(math.exp(math.log(s1) - math.log(s2)))
