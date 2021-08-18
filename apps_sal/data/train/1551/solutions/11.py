n = int(input())
while n > 0:
    s1 = list(input().split())
    flag = 0
    for i in range(0, len(s1)):
        if str(s1[i]) == "not":
            flag = 1
    if flag == 1:
        print("Real Fancy")
    else:
        print("regularly fancy")
    n = n - 1
