# cook your dish here
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
    l[i].sort()
countu = 0
for i in l:
    if l.count(i) == 1:
        countu += 1
print(countu)
