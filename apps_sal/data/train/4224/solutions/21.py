def dont_give_me_five(start, end):
    array = list(range(start, end + 1))
    out = [num for num in array if not '5' in str(num)]
    return len(out)
