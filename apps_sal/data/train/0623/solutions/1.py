# cook your dish here
n = int(input())
lst = []
for i in range(n):
    i = int(input())
    lst.append(i)

lst.sort()
for i in range(n):
    print(lst[i])
