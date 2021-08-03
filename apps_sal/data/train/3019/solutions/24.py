def str_count(strng, letter):
    x = list(strng)
    y = 0
    for k in x:
        if k == letter:
            y += 1
        else:
            y += 0
    return y
    # Your code here ;)
