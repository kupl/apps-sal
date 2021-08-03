t = int(input())
for i in range(t):
    list1 = []
    for i in range(3):
        list1.append(list(map(int, input().split())))
    min1 = min(list1[0][0], list1[1][0], list1[2][0])
    min2 = min(list1[0][1], list1[1][1], list1[2][1])
    min3 = min(list1[0][2], list1[1][2], list1[2][2])
    max1 = max(list1[0][0], list1[1][0], list1[2][0])
    max2 = max(list1[0][1], list1[1][1], list1[2][1])
    max3 = max(list1[0][2], list1[1][2], list1[2][2])
    list2 = []
    list3 = []
    list2 = [min1, min2, min3]
    list3 = [max1, max2, max3]
    if((list2 not in list1) or (list3 not in list1)):
        print("no")
    elif((list2 in list1) and (list3 in list1)):
        list1.remove(list2)
        list1.remove(list3)
        if(list1[0] != list2 and list1[0] != list3):
            print("yes")
        else:
            print("no")
