# return count of occurrences the 2nd argument is found in the first one
# input - two strings
# output - integer
# edge cases - empty strings for first argument, in that case return 0


def str_count(strng, letter):
    # start counting from 0
    count = 0
# loop over every element in string
    for e in strng:
        # if element is equal to letter in second argument
        if e == letter:
            # add element to the count
            count += 1
# return count of letter in string
    return count
