# cook your dish here
n = int(input())
a = []
for i in range(0, n):
    no = int(input())
    a.append(no)
a.sort()
for i in range(0, n):
    print(a[i])
