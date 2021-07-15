'''input
5 2
1
3
3
9
4
'''

l = list(map(int, input().split(" ")))
n, d = l[0], l[1]

n_list = []
for i in range(n):
 n_list.append(int(input()))

n_list.sort()

knt = 0
i=1
while i<n:
 if n_list[i] - n_list[i-1] <= d:
  knt += 1
  i += 2
  continue

 i += 1
print(knt)
