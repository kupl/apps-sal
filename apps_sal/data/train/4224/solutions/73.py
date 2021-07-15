def dont_give_me_five(start,end):
    return sum([1 if '5' not in str(i) else 0 for i in [loop for loop in range(start, end + 1)]])
