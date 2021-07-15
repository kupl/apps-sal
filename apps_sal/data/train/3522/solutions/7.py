def max_gap(numbers):
    numbers.sort()
    i = 0
    res =[]
    while i <len(numbers)-1:
        if len(numbers)>=0:
            n =abs(numbers[i]-numbers[i+1])
            res.append(n)
        i+=1
    return max(res)
