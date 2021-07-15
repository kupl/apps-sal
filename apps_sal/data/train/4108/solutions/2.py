def sum_even_numbers(seq): 
    return sum(filter(lambda n: n%2==0, seq))
