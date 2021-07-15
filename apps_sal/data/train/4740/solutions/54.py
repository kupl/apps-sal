def row_sum_odd_numbers(n:int)->int:
    """[Find the sum of a row based on odd number pyramid]

    Args:
        n (int): [Row Number starting from 1]

    Returns:
        int: [Sum of Row]
    """
    num_of_records = n*(n+1)//2
    return sum([2*i-1 for i in range(num_of_records -n+1,num_of_records+1)])

