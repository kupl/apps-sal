from collections import Counter
n=int(input())
for i in range(n):
    k=list(input())
    c=Counter(k)
    print(c['4'])
