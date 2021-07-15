def arr(n=0): 
    lst = []
    if n > 0:
        for n in range(n):
            lst.append(n)
        print(lst)
        return lst
    else:
        return lst
        
print(arr())
