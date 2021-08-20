def dont_give_me_five(start, end):
    for i in range(end, start - 1, -1):
        end -= '5' in str(i)
    return end - start + 1
