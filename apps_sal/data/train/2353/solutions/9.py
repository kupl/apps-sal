n = int(input())
l = [int(i) for i in input().split(' ')]
index = []
nums = sorted(l)
for i in l:
    index.append(nums.index(i))
indexbis = [int(i - 1) for i in index]
for i in range(n):
    if indexbis[i] == min(indexbis):
        indexbis[i] = n - 1
        break
for i in indexbis:
    print(l[index.index(i)], end=' ')
