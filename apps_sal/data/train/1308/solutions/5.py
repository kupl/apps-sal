
def findPassword():
    flag = 0
    t = 1
    m = "Invalid"
    while(m != "Valid"):
        x = input()
        t = 1
        flag = 0
        for i in x:
            if x.count(i) > 1:
                print("Invalid")
                t = 0
                break
            if i.isdigit():
                flag = 1
        if flag == 1 and t != 0:
            print("Valid")
            m = "Valid"


findPassword()
