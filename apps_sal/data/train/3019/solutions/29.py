def str_count(strng, letter):
    # Your code here ;)
    count = 0
    
    for alphabet in strng:
        if letter == alphabet:
            count += 1
    return count

