def Remove(duplicate):
    result = []
    for num in duplicate:
        if num not in result:
            result.append(num)
    return result
    
def min_value(digits):
    digits = Remove(digits)
    digits = sorted(digits)
    min = ''
    for i in digits:
        min += str(i)
    return int(min)     
