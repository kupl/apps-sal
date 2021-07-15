def divisible_by(numbers, divisor):
    """(list<int> -> list<int>)
    Returns the list of members of numbers list divisible by the passed divisor.
    >>> [1,2,3,4,5,6], 3)
    [3,6]
    
    >>> [1,3,5], 2)
    []
    
    >>> [0], 4)
    [0]
    """
    divisibleNums = []
    for num in numbers:
        if((num % divisor) == 0):
            divisibleNums.append(num)

    return divisibleNums
