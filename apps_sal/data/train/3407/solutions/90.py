def palindrome_chain_length(n):

    number = n
    i = 0
    while i < 10000:
        number = str(number)
        if number == number[::-1]:
            return i
        else:
            number = int(number) + int(number[::-1])
            i = i + 1
