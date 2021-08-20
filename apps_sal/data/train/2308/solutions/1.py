from collections import deque
import sys
input = sys.stdin.readline
(n, w) = [int(i) for i in input().rstrip('\n').split()]
arr = []
tem = []
for i in range(n):
    t = [int(i) for i in input().rstrip('\n').split()]
    tem.append(t[0])
    arr.append(t[1:])
l = [0 for i in range(w)]
wi = [0 for i in range(w + 1)]
for j in range(n):
    st = deque()
    c = w - tem[j]
    for i in range(tem[j]):
        while st and st[0] < i - c:
            st.popleft()
        while st and arr[j][st[-1]] < arr[j][i]:
            st.pop()
        st.append(i)
        if arr[j][st[0]] > 0 or (i >= c and i < w - c):
            l[i] += arr[j][st[0]]
    ind = tem[j]
    while st and arr[j][st[0]] > 0:
        wi[ind] += arr[j][st[0]]
        wi[w - (tem[j] - st[0]) + 1] += -arr[j][st[0]]
        ind = w - (tem[j] - st[0]) + 1
        st.popleft()
curr = 0
for i in range(w):
    curr += wi[i]
    l[i] += curr
print(' '.join((str(e) for e in l)))
