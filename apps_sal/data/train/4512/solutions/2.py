
def find_num(n):
    c = 0
    k = -1
    mas = []
    while len(mas) <= n:
        k += 1
        if  k > 10:
            c = set(str(mas[len(mas)-1]))
            if len(c) == len(set(str(mas[len(mas)-1]))-set(str(k))) and k not in mas:
                mas.append(k)
                k = 10    
        else:
            mas.append(k)
    return mas[len(mas)-1]
            
        
                    
                    
                    
            

