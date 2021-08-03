def routne(s):
    flag = 0
    for i in range(len(s) - 1):
        if ord(s[i]) > ord(s[i + 1]):
            flag = 0
            return "no"
        else:
            flag = 1
    if flag == 1:
        return "yes"
    else:
        return "no"


for i in range(int(input())):
    a = input()
    print(routne(a))
