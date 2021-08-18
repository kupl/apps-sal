
import sys
inf = float("inf")


abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod, MOD = 1000000007, 998244353
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


q = int(input())
while q > 0:
    n = int(input())
    Arr = get_array()
    mydict = dict()
    for i in Arr:
        mydict[i] = mydict.get(i, 0) + 1
    myset = set()
    count = 0
    for i in mydict:
        if mydict[i] not in myset:
            count += mydict[i]
            myset.add(mydict[i])
        else:
            z = mydict[i]
            for i in range(z, 0, -1):
                if i not in myset:
                    count += i
                    myset.add(i)
                    break
    print(count)
    q -= 1
