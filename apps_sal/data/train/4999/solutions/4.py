def capital(capitals): 
    list1 = []
    for i in capitals:
        a = list(i.values())
        print(a)
        list1.append("The capital of " + a[0] + " is " + a[1])
    return list1

