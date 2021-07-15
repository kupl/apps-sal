def dont_give_me_five(start,end):
    # your code here
    return sum ('5' not in str(i) for i in range(start, end + 1))  # amount of number
