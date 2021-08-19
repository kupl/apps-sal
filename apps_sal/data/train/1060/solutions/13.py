# cook your dish here
for _ in range(int(input())):
    N = int(input())
    l = input()
    arr1 = []
    arr2 = []
    #total = sum(arr1)
    # print(total)
    count1 = 0
    count2 = 0
    for i in range(len(l) - 1, -1, -1):
        if(l[i] == '0'):
            arr1.append(count1)
            count2 += 1
        elif(l[i] == '1'):
            count1 += 1
            arr2.append(count2)
    print(sum(arr1) + sum(arr2))
