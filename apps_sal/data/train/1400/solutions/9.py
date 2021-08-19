# cook your dish here
from sys import stdin, stdout
input = stdin.readline
print2 = stdout.write
def get_ints(): return map(int, stdin.readline().split())
def get_list(): return list(map(int, stdin.readline().split()))


for _ in range(int(input())):
    n, l, r = get_ints()
    numsR = [2**i for i in range(r)]
    if l != r:
        numsL = [2**i for i in range(l)]
    else:
        numsL = numsR
    ma = sum(numsR) + (n - r) * numsR[-1]
    mi = sum(numsL) + n - l
    print(mi, ma)
