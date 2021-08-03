a = list(input())
n = len(a)
for i in range(n):
    if(a[i] == 'r'):
        print(i + 1)
for i in range(n - 1, -1, -1):
    if(a[i] == 'l'):
        print(i + 1)
