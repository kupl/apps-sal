t = int(input())
while t > 0:
    inp = input()
    arr = input()
    inp = inp.split()
    n = int(inp[0])
    z1 = int(inp[1])
    z2 = int(inp[2])
    arr = arr.split()
    arr = [int(value) for value in arr]
    for i in range(n):
        arr.append(-1 * arr[i])
    flag = 0
    for val in arr:
        if val == z1 or val == z2:
            flag = 1
            print(1)
            break
    cnt = 0
    for val1 in arr:
        if val1 - z1 in arr or val1 - z2 in arr:
            cnt += 1
    if cnt == len(arr) and (not flag == 1):
        flag = 2
        print(2)
    if flag == 0:
        print(0)
    t -= 1
