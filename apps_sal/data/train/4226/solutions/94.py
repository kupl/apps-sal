def remove_smallest(numbers):
    print(numbers)
    
    numlist = numbers.copy()
    
    if len(numlist) <= 1:
        return []
    else:
        for i in numlist:
            if i == min(numlist):
                if numlist.count(i) >= 1:
                    numlist.remove(i)
                    break
                else:
                    pass
    
    return numlist

