def remove_smallest(numbers):
    if len(numbers) == 0:
        return(numbers)
    smvalue = numbers[0]
    smindex = 0
    if len(numbers) > 1:
        for i in range(1, len(numbers)):
            if numbers[i] < smvalue:
                smvalue = numbers[i]
                smindex = i
        return(numbers[0:smindex] + numbers[(smindex + 1):len(numbers)])
    else:
        return(list())
