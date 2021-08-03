from bisect import bisect_left, insort_left
n = int(input())
s = list(input())
lindex = [[] for _ in range(26)]
for i in range(n):
    lindex[ord(s[i]) - 97].append(i)
q = int(input())
for i in range(q):
    q1, q2, q3 = input().split()
    if q1 == '1':
        q2 = int(q2) - 1
        idx = bisect_left(lindex[ord(s[q2]) - 97], q2)
        if s[q2] != q3:
            del lindex[ord(s[q2]) - 97][idx]
            insort_left(lindex[ord(q3) - 97], q2)
            s[q2] = q3
    else:
        l = int(q2) - 1
        r = int(q3) - 1
        cnt = 0
        for j in range(26):
            if len(lindex[j]) == 0:
                continue
            idx = bisect_left(lindex[j], l)
            if len(lindex[j]) > idx and lindex[j][idx] <= r:
                cnt += 1
        print(cnt)
