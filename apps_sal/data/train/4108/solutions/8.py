def sum_even_numbers(seq): 
    sum = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            sum += seq[i]
    return sum
