from sys import stdin as sin
def aint(): return int(input())
def amap(): return map(int, sin.readline().split())
def alist(): return list(map(int, sin.readline().split()))
def astr(): return input()


for _ in range(int(input())):
    s = input()
    print(len(set(s)))
