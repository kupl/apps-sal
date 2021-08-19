arr = [float(i) for i in input().split()]
n = int(arr[0])
for i in range(1, 2 * n + 1, 2):
    a = arr[i]
    p = arr[i + 1]
    jk = 10 ** p
    pk = jk * a * 1.0
    print('{:0.2f}'.format(pk))
