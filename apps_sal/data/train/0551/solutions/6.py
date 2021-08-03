t = int(input())
for i in range(t):
    s = input()
    list1 = []
    flag = 0
    for i in range(len(s)):
        list1.append(s[i])
    set1 = set(list1)
    dict1 = dict()
    for i in set1:
        dict1[i] = 0
    for i in list1:
        dict1[i] += 1
        if(dict1[i] > 1):
            print("yes")
            flag = 1
            break
    if(flag == 0):
        print("no")
