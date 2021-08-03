while True:
    x = input()
    dic = {}
    for i in range(len(x)):
        if x[i] in dic:
            dic[x[i]] += 1
        else:
            dic[x[i]] = 1
    if len(dic) == len(x):
        if x.isalnum() == True:
            print("Valid")
            break
        else:
            print("Invalid")
    else:
        print("Invalid")
