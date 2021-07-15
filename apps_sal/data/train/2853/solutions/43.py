def solve(arr):
    res = []
    for number in arr[::-1]:
        if number not in res:
            res.append(number)
        else:
            pass
    return res[::-1]
            
            

