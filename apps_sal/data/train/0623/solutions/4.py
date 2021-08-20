t = int(input())
lst = []
for i in range(t):
    lst.append(int(input()))
lst.sort()
for i in range(t):
    print(lst[i])
