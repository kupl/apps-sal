def list_squared(m, n):
    def f(number):
        divisor_list = []
        n = int(number ** 0.5) + 1
        for e in range(1,n):
            if number % e == 0:
                if int(number / e) == e:
                    divisor_list.append(e**2)
                else:
                    divisor_list.append(e**2)
                    divisor_list.append((int(number / e))**2)
    
        summation = sum(divisor_list)
    
        if int(summation ** 0.5) == float(summation ** 0.5):
            return [True,summation]
        else:
            return [False,summation]
    list = []
    for i in range(m, n):
        d_l = f(i)
        if d_l[0]:
            list.append([i,d_l[1]])
    return list



                       
                       

