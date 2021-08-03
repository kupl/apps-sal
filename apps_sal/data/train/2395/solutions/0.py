for _ in range(int(input())):
    n = int(input())
    s = input()
    a = ""
    b = ""
    flag = 1
    for i in s:
        if flag:
            if i == "2":
                a += "1"
                b += "1"
            elif i == "1":
                a += "1"
                b += "0"
                flag = 0
            else:
                a += "0"
                b += "0"
        else:
            if i == "2":
                a += "0"
                b += "2"
            elif i == "1":
                a += "0"
                b += "1"
                flag = 0
            else:
                a += "0"
                b += "0"
    print(a)
    print(b)
