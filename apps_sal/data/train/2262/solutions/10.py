from collections import deque
r, c, n = [int(item) for item in input().split()]
on_edge = [[] for _ in range(4)]
for i in range(n):
    x1, y1, x2, y2 = [int(item) for item in input().split()]
    v1_on_edge = x1 == 0 or x1 == r or y1 == 0 or y1 == c 
    v2_on_edge = x2 == 0 or x2 == r or y2 == 0 or y2 == c 
    if v1_on_edge and v2_on_edge:
        if x1 == 0:
            on_edge[0].append([y1, i])
        elif x1 == r:
            on_edge[2].append([y1, i])
        elif y1 == 0:
            on_edge[3].append([x1, i])
        elif y1 == c:
            on_edge[1].append([x1, i])
        if x2 == 0:
            on_edge[0].append([y2, i])
        elif x2 == r:
            on_edge[2].append([y2, i])
        elif y2 == 0:
            on_edge[3].append([x2, i])
        elif y2 == c:
            on_edge[1].append([x2, i])
for i in range(4):
    if i <= 1:
        on_edge[i].sort()
    else:
        on_edge[i].sort(reverse=True)
total = [item for line in on_edge for item in line]        
st = deque()
st.append(-1)
for val, item in total:
    if st[-1] == item:
        st.pop()
    else:
        st.append(item)
if st[-1] == -1:
    print("YES")
else:
    print("NO")


