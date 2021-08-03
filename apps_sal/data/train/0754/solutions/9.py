
for _ in range(int(input())):
    k = input()
    flag = 0
    a = ['0', '2', '4', '6', '8']
    for i in k:
        if i in a:
            flag = 1
            break
    if flag == 1:
        print("1")
    else:
        print("0")
