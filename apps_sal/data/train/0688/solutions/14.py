def uniformString(s):
    res = s.count('10') + s.count('01')
    if res <= 2:
        print('uniform')
    else:
        print('non-uniform')
    return


t = int(input())
for _ in range(t):
    s = input()
    uniformString(s)
