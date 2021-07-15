def max_tri_sum(numbers):
    return sum(sorted(list(dict.fromkeys(numbers)))[-3:])
    #your code here

