import math
import re


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-9


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


n = ri()
mp = {}
ar=[]
for i in range(401,-1,-1):
    ar.append(('k'*i+'h'))

for i in range(n):
    st = input()
    st = st.replace('u', 'oo')

    for j in range(1,len(ar)):
        st=st.replace(ar[j-1],ar[j])

    mp[st] = 1
print(len(mp))

