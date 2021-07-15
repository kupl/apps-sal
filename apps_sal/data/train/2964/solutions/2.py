def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None 
    for n in numbers: 
        if not smallest1 or n < smallest1: 
            smallest2 = smallest1
            smallest1 = n 
        elif not smallest2 or n < smallest2: 
            smallest2 = n 
    return smallest1 + smallest2
