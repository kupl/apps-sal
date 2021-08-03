def str_count(strng, letter):
    # Your code here ;)
    i = 0
    n = 0
    while i <= len(strng) - 1:
        for j in strng:
            if j == letter:
                n = n + 1

        i = i + 1
        return n
