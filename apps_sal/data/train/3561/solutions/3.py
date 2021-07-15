
def around_fib(n):
    fiblist = [0,1]
    if n>1:
        for i in range(2,n+1):
            fiblist.append(fiblist[-1]+fiblist[-2])
    list1 = [int(i) for i in str(fiblist[-1])]
    list2 = []
    for i in range(10):
        count = list1.count(i)
        list2.append(count)
    for i in range(10):
        if list2[i] == max(list2):
            max1 = i
            max2 = max(list2)
            break
    list3 = []
    list4 = []
    x = len(list1)//25
    if len(list1)%25 != 0:
        for i in range(x*25,len(list1)):
            list3.append(list1[i])
    else:
        i = -1
        while len(list3)<25:
            list3.append(list1[i])
            i-=1
        list3.reverse()
                
    return "Last chunk "+"".join([str(i) for i in list3])+"; Max is "+str(max2)+ " for digit " + str(max1)
