def remove_smallest(numbers):
    if numbers == []:
        return []
    m = min(numbers)
    res = numbers.copy()
    for i in range(0, len(numbers)):
        if res[i] == m:
            del res[i]
            break
    return res
        

