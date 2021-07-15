def divisible_by(numbers, divisor):
    list1=[]
    for i in range (len(numbers)+1):
        if i % divisor == 0 and i in numbers :
                list1.append(i)
    return list1
