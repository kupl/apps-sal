tc = int(input())
while tc != 0:
    (r, c) = map(int, input().split())
    arr = []
    for i in range(r):
        temp = list(map(int, input()))
        arr.append(temp)
    count = 0
    for j in range(c):
        temp = 0
        for i in range(r):
            if arr[i][j] == 1:
                temp += 1
        if temp != 1 and temp != 0:
            count += temp * (temp - 1) // 2
    print(count)
    tc -= 1
