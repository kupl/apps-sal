# cook your dish here
from sys import stdin, stdout


def lin(): return int(stdin.readline())
def mlin(): return map(int, stdin.readline().rstrip().split())
def llin(): return list(mlin())


def res():
    for i in range(lin()):
        v1, t1, v2, t2, v3, t3 = mlin()
        if v1 + v2 < v3:
            print("NO")
        else:
            x = (v3 * (t3 - t2)) / (t1 - t2)
            y = (v3 * (t3 - t1)) / (t2 - t1)
            if x <= v1 and y <= v2 and x >= 0 and y >= 0:
                print("YES")
            else:
                print("NO")


res()
