def dont_give_me_five(start, end):
    # your code here
    m = [i for i in range(start, end + 1) if "5" not in str(i)]
    return len(m)   # amount of numbers
