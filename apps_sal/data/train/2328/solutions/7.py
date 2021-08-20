import sys


def subsetsum(array, num):
    if num == 0 or num < 1:
        return False
    elif len(array) == 0:
        return False
    elif array[0] == num:
        return True
    else:
        return subsetsum(array[1:], num - array[0]) or subsetsum(array[1:], num)


(n, q) = [int(i) for i in sys.stdin.readline().split()]
l = [int(i) for i in sys.stdin.readline().split()]
while q > 0:
    q -= 1
    s = []
    s = [int(i) for i in sys.stdin.readline().split()]
    if s[0] == 3:
        l1 = s[1]
        r = s[2]
        w = s[3]
        if subsetsum(l[l1 - 1:r], w) == True:
            sys.stdout.write('Yes\n')
        else:
            sys.stdout.write('No\n')
    elif s[0] == 2:
        l1 = s[1]
        r = s[2]
        i = l1 - 1
        j = r - 1
        while i < j:
            (l[i], l[j]) = (l[j], l[i])
            j -= 1
            i += 1
    else:
        i = s[1]
        x = s[2]
        l[i - 1] = x
