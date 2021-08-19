def correct_tail(body, tail):
    # calculate the index of the last letter from the string
    index = len(body) - 1
    # assign the last letter of the string to the variable
    last_letter = body[index]
    # compare the last letter of the string with the tail
    if (last_letter == tail):
        return True
    else:
        return False
