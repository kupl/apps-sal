def remove_smallest(numbers):
    num = numbers.copy()
    l = len(num)
    if num != []:
        smol = min(num)
        i = 0
        for i in range(0,l):
            if num[i] == smol:
                num.pop(i)
                break
            else: i += 1  
        return num
    else: return []
