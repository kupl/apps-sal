# cook your dish here
arr = [1]
for i in range(1, 18):
    x = 6**i
    b = [x]
    for j in arr:
        b.append(j + x)
    arr += b
arr.sort()
for t in range(int(input())):
    n = int(input())
    print(arr[n - 1])
