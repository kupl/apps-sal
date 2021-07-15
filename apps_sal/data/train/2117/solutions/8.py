n = int(input())
a = [0] + list(map(int,input().split())) + [0]
r = [0] * (n + 1)
st = [(0, 0)]
for i in range(1, n + 2):
 	while a[i] < st[-1][0]:
  		r[i - st[-2][1] - 1] = max(st[-1][0], r[i - st[-2][1] - 1])
  		st.pop()
 	st.append((a[i], i))
for i in range(n): r[-i - 2] = max(r[-i - 2], r[-i - 1])
print(*r[1:]) 
