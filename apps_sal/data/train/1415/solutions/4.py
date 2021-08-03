import sys


def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    flag1 = 1
    flag2 = 1
    s = input()
    i = 0
    j = len(s) - 1
    while(i <= j):
        if(s[i] != s[j]):
            break
        i = i + 1
        j = j - 1
    if(i > j):
        print('YES')
        continue
    k = i
    m = j
    i = i + 1
    while(i <= j):
        if(s[i] != s[j]):
            flag1 = 0
            break
        i += 1
        j -= 1
    i = k
    j = m - 1
    while(i <= j):
        if(s[i] != s[j]):
            flag2 = 0
            break
        i += 1
        j -= 1

    if(flag1 or flag2):
        print('YES')
    else:
        print('NO')
