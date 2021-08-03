# cook your dish here
n, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mini = float('inf')
maxi = -float('inf')
maxi_ind = -1
mini_ind = -1

for i in range(n):
    if a[i] < mini:
        mini = a[i]
        mini_ind = i

for i in range(z):
    if b[i] > maxi:
        maxi = b[i]
        maxi_ind = i

for i in range(n):
    if i == mini_ind:
        for j in range(z):
            print(i, j)
    else:
        print(i, maxi_ind)
