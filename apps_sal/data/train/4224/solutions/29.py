def dont_give_me_five(start, end):
    # Set position and create list
    position = start
    count = []

    # Check if numbers have a 5 in them and skip
    # append all other numbers to list
    while position <= end:
        if '5' in str(position):
            position += 1
        else:
            count.append(position)
            position += 1

    # Return length of list
    return len(count)
