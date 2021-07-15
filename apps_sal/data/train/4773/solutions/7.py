def multiplyList(myList) : 
      
    result = 1
    for x in myList: 
         result = result * x  
    return result 
def count_find_num(primesL, limit):
    base = multiplyList(primesL)
    primesL.sort()
    list1 = [base]
    i = base
    for i in primesL:
        for j in list1:
            d = j
            while d<limit:
                d=d*i
                if d<=limit:
                    list1.append(d)
    if len(list1)==1 and list1[0]>limit:
        return []
    else:
        list2 = list(set(list1))
        return [len(list2),max(list2)]

