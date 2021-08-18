"""
s_reated on Sat May 30 19:42:30 2020

@author: trinzya
"""

import string


t = int(input())
for i in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    s = []
    c = []
    count = 0
    s_ = []

    if not set(b).issubset(set(a)):
        print(-1)
        continue

    abs_ = string.ascii_lowercase

    for k in range(len(abs_) - 1, -1, -1):
        flag = 0
        f = 0
        j = abs_[k]
        if a == b:
            break
        if j not in c:
            s = []
            for i in range(n):

                if ((a[i] != b[i]) and (b[i] == j) and (a[i] > j)):
                    f = 1
                    s.append(i)
                if a[i] == j:
                    flag = 1
                    s.append(i)

            if len(s) != 0:
                count = count + 1
                if len(s) == 1:

                    s = []
                    count = count - 1
                    continue
                if (flag == 0 and f == 1) or (flag == 1 and f == 0):

                    count = count - 1
                    continue
                for i in s:

                    a[i] = j

                s_.append(s)
            c.append(j)
    if a != b:
        print(-1)
        continue

    print(count)
    if count != 0:
        for i in s_:
            i = list(map(str, i))
            print(len(i), " ".join(i))
