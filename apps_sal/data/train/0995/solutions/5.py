n = int(input())
l = list(map(int, input().split()))
k = int(input())
scores = []
length = len(l)
for i in range(k + 1):
    l1 = l[0:i]
    l2 = l[length - (k - i):]
    scores.append(sum(l1) + sum(l2))
print(max(scores))
