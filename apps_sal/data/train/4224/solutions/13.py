def dont_give_me_five(start, end):
    # your code here
    n = end - start + 1
    for i in range(start, end+1):
        if '5' in str(i):
            n -= 1
    return n
