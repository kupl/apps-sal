# cook your dish here
import collections
n, q, k = map(int, input().split())
a = list(map(int, input().split()))
st = str(input())
de = collections.deque(a)
for f in range(q):
    if st[f] == '!':
        de.rotate(1)
    else:
        mi = 0
        prev = 0
        cnt = 0
        while 1:
            i = prev
            if de[i] == 1:
                while de[i] == 1:
                    cnt += 1
                    i += 1
                    if i > n - 1:
                        break
            else:
                i += 1
            prev = i
            if cnt > mi:
                mi = cnt
            if prev >= n - 1:
                break
            cnt = 0
        if mi < k:
            print(mi)
        else:
            print(k)
