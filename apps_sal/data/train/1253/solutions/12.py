# cook your dish here

def spread(arr):
    for i in range(len(arr)):
        a = list()
        for j in range(len(arr[i])):
            if arr[i][j][0] == 1:
                a.append(j)
        for j in range(len(a)):
            if j == 0 and a[j] == 0 and len(arr[i]) > 1:
                arr[i][1][0] = 1
            elif j == len(a) - 1 and a[j] == len(arr[i]) - 1 and len(arr[i]) > 1:
                arr[i][a[j] - 1][0] = 1
            elif a[j] != 0 and a[j] != len(arr[i]) - 1:
                arr[i][a[j] - 1][0] = arr[i][a[j] + 1][0] = 1


t = int(input())
for z in range(t):
    n = int(input())
    inp = input()
    a = [0] * n
    for i in range(n):
        a[i] = [0] * 2
        a[i][0] = int(inp[i])
        a[i][1] = i
    d = int(input())
    arr = [a]
    fr = input().split()
    for i in range(d):
        fr[i] = int(fr[i])
        fr[i] -= 1
        for j in range(len(arr)):
            if arr[j][len(arr[j]) - 1][1] >= fr[i]:
                start = j
                break
        l = list()
        j = 0
        while fr[i] > arr[start][j][1]:
            l.append(arr[start][j])
            j += 1
        arr.insert(start, l)
        for j in range(len(l)):
            arr[start + 1].remove(l[j])
        spread(arr)
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][0] == 1:
                count += 1
    print(count)
