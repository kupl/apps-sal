def tri(arr, n):
    li1 = []

    arr = sorted(arr)
    z = 0
    for i in range(n - 2):
        li = []
        if(arr[i] + arr[i + 1] > arr[i + 2]):
            li.append(arr[i])
            li.append(arr[i + 1])
            li.append(arr[i + 2])
            z = 1
        else:
            pass
        li1.append(li)
    if(z == 0):
        print('NO')
    else:
        print('YES')
        m = sorted(max(li1), reverse=True)
        print(*m, sep=' ')


n = int(input())
a = [int(x) for x in input().split()]
#print('YES' if tri(a, n) else 'NO')
tri(a, n)
