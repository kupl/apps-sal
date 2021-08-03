n, k = map(int, input().split())
l = map(int, input().split())
l = [int(x) for x in l]
flag = True
result = []
if sum(l) % k != 0:
    flag = False
    print("No")
else:
    length = sum(l) / k
    s = 0
    for i in range(len(l)):
        s += l[i]
        if s > length:
            print("No")
            flag = False
            break
        elif s == length:
            result.append(i + 1)
            s = 0
    if flag == True:
        print("Yes")
        for i in range(len(result) - 1, 0, -1):
            result[i] -= result[i - 1]
        for number in result:
            print(number, end=" ")
