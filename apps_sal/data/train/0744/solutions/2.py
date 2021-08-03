arr = ["*"]
for i in range(105):
    arr.append("*" + " " * i + "*")

t = int(input())
for i in range(t):
    k = int(input())
    k = (k + 1) // 2
    for i in range(k):
        print(arr[i])
    for i in range(k - 2, -1, -1):
        print(arr[i])
