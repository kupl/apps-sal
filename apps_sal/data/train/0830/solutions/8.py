# cook your dish here
def conv(a, b):
    stop = 0
    n = len(a)
    for i in range(0, n):
        if ord(a[i]) - ord(b[i]) < 0:
            print(-1)
            stop = 1

    if stop == 0:
        for i in range(0, n):
            flag = 0
            for j in range(0, n):
                if b[i] == a[j]:
                    flag = 1
                    break
            if flag == 0:
                print(-1)
                stop = 1
                break
    if stop == 0:
        distinctArr = []
        for i in range(0, n):
            dontAdd = 0
            if a[i] != b[i]:
                for j in range(0, len(distinctArr)):
                    if b[i] == distinctArr[j]:
                        dontAdd = 1
                if dontAdd == 0:
                    distinctArr.append(b[i])
        distinctArr.sort(reverse=True)
        print(len(distinctArr))

        for i in range(0, len(distinctArr)):
            arr = []
            for j in range(0, n):
                if distinctArr[i] == b[j] and b[j] != a[j]:
                    arr.append(j)
            for j in range(0, n):
                if distinctArr[i] == a[j]:
                    arr.append(j)
                    break
            arr.sort()
            print(len(arr), end=" ")
            for k in range(0, len(arr)):
                if k == len(arr) - 1:
                    print(arr[k])
                else:
                    print(arr[k], end=" ")
        # print(distinctArr)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = input()
    b = input()
    arr1 = list(a)
    arr2 = list(b)
    conv(arr1, arr2)
