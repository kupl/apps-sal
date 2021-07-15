def arr(*n): 
    # [ the numbers 0 to N-1 ]
        print(*n)
        res = []
        if(n == () or n == 0):
            return []
        else:
            for i in range((*n)):
                res.append(i)
            return res
