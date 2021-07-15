import sys
def sum_two_smallest_numbers(numbers):
    num = []
    num = numbers
    firstnum = sys.maxsize
    secondnum = sys.maxsize
    sum = 0
    for i in range(0,len(num)):
        if num[i] < firstnum:
            firstnum = num[i]
            
        else:
            {}
    for i in range(0,len(num)):
        if num[i] == firstnum:
            {}
        elif num[i] < secondnum:
            secondnum = num[i]
            
        else:
            {}
    sum = firstnum+secondnum
    return sum
    

