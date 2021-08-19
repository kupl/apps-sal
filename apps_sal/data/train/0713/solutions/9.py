# cook your dish here
x = int(input())
for i in range(x):
    y = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    k = 0
    c = 0
    for j in range(y):
        if (a[j] == b[k]):
            k = k + 1
            if(k == m):
                c = 1
                print('Yes')
                break
    if(c == 0):
        print('No')
