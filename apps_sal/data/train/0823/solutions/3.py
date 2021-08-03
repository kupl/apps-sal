# cook your dish here
for _ in range(int(input())):
    arr = list(map(int, input().strip().split()))
    flag = 1
    for p in range(1, 16):
        sum = 0
        for i in range(0, 4):
            f = 1 << i
            if (p & f) != 0:
                sum += arr[i]
        if sum == 0:
            flag = 0
            print("Yes")
    if flag == 1:
        print("No")
