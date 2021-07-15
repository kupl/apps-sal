def capital(capitals): 
    # your code here
    q = []
    lst = []
    p = len(capitals)
    for i in capitals:
          for key,value in i.items():
              var1 = value
              q.append(var1)
    lst2 = []
    for x,y in enumerate(q,1):
        lst.append(y)
        if x % 2 == 0:
            lst2.append("The capital of {} is {}".format(lst[0],lst[1]))
            lst.clear()
    return lst2    
