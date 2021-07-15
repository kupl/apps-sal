from collections import Counter
n = int(input())
x = [0]
for v in map(int, input().split()):
    x.append(x[-1] ^ v)
c0 = Counter(x[::2])
c1 = Counter(x[1::2])
r = 0
for v in c0.values():
    r += v*(v-1)//2
for v in c1.values():
    r += v*(v-1)//2
print(r)    
