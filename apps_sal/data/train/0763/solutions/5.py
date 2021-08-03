# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    p = input().strip()
    arr1 = [0] * (n + 1)
    arr2 = [0] * (n + 1)
    flag = False
    s1 = 0
    p1 = 0
    for i in range(1, n + 1):
        arr1[i] = arr1[i - 1]
        arr2[i] = arr2[i - 1]
        if s[i - 1] == '1':
            arr1[i] += 1
            s1 += 1
        if p[i - 1] == '1':
            arr2[i] += 1
            p1 += 1

        if arr1[i] < arr2[i]:
            flag = True
            break
    # print(arr1)
    # print(arr2)
    if p1 != s1:
        flag = True
    if flag:
        print("No")
    else:
        print("Yes")
