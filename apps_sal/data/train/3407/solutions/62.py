def palindrome_chain_length(total):
    counter = 0
    reverse_total = str(total)[::-1]
    while total != int(reverse_total):
        total = total + int(reverse_total)
        reverse_total = str(total)[::-1]
        counter +=1
    return counter
