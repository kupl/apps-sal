def str_count(strng, letter):
    arr = list(strng)
    i = 0
    for item in arr:
        if item == letter:
            i += 1
    return i

    # Your code here ;)
