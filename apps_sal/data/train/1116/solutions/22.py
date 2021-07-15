N = int(input())
A= list(map(int,input().split(' ')))
s = 0
prefixsums = [0]
for x in A:
 prefixsums.append(prefixsums[-1] + x)
freq = {}
for y in prefixsums:
 if y in freq:
  freq[y] += 1
 else:
  freq[y] = 1
print(sum(v*(v-1) // 2 for v in freq.values()))
