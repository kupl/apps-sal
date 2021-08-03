n, q = list(map(int, input().split()))
arr = [int(n) for n in input().split()]
x = arr[0]
arr1 = []
arr1.append(x)
for i in range(1, n):
    x = x ^ arr[i]
    arr1.append(x)
arr1.append(0)
while(q):
    q = q - 1
    x = int(input())
    r = x % (n + 1)
    print(arr1[r - 1])
