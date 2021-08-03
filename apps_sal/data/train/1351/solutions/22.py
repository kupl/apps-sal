def itguy(arr):
    for i in range(0, len(arr)):
        if(arr[i] == None):
            arr[i] = 0
        elif(arr[i] != 0):
            arr[i] = i
            for j in range(i + 1, len(arr)):
                if(arr[j] == i):
                    arr[j] = 0
    for i in arr:
        print(i, end=" ")
    print()


n = int(input())
for i in range(n):
    l = int(input())
    arr = list(map(float, input().split()))
    itguy(arr)
