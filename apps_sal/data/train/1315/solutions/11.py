n = int(input())
lst = []
unique = 0
for _ in range(n):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    lst.append(a)
for ele in lst:
    if lst.count(ele) == 1:
        unique += 1
print(unique)
