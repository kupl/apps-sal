def men_from_boys(arr):
    even = []
    odd = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd[::-1]
    
    

