# cook your dish here
n = int(input())
lst = []

for i in range(n):
    l1 = list(map(int, input().split()))
    l1.sort()
    if l1 not in lst:
        lst.extend([l1])
    else:
        lst.remove(l1)


print(len(lst))
