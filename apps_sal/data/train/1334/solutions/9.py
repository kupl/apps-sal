# cook your dish here
n = int(input())
a = list(map(int, input().split()))
node = [0] * n
if(n == 1):
    print(a[0])
elif(n == 2):
    print(min(a[0], a[1]))
elif(n == 3):
    print(min(a[0], a[1], a[2]))
else:
    node[n - 1] = a[n - 1]
    node[n - 2] = a[n - 2]
    node[n - 3] = a[n - 3]
    for i in range(n - 4, -1, -1):
        node[i] = min(node[i + 1], node[i + 2], node[i + 3]) + a[i]

    print(min(node[0], node[1], node[2]))
