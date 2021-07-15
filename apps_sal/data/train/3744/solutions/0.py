def oddest(numbers):
    most_odd   = 0      # The current most odd number in the list
    max_oddity = -1     # The current greatest oddity rate, starts at -1 so that even an even number can be the unique most odd
    is_unique  = True   # If the current most odd number is really the most, so if there is no unique oddest number, it will return None
    for num in numbers:  # Loop through all the numbers
        oddity  = 0      # The oddity rate starts at 0
        print(num)
        insider = num    # The coefficient of the number 2, so in 2n + 1, the insider is n
        while insider % 2 == 1:  # While that coefficient is odd
            if insider == -1:
                oddity = 1 + max([abs(n) for n in numbers]) # Since the oddity rate of a number is NEVER greater than the absolute value of the number, this garantees that the current number is the most odd one
                break
            else:
                oddity  += 1               # Add the oddity rate of the total number
                insider = (insider-1)/2    # So if in 2n + 1, n is odd, represent it as 2(2m + 1) + 1, and set the value to m
        if oddity > max_oddity:  # If the current number's oddity rate is greater than the current max oddity,
            is_unique = True     # Set it to unique
            max_oddity = oddity  # Set the max oddity to the current oddity
            most_odd   = num     # Set the most odd number to the current number
        elif oddity == max_oddity:# Otherwise, if it's the same rate
            is_unique = False    # It's not unique
    if is_unique and max_oddity >= 0:  # If the current most odd number is REALLY the most odd number and the list isn't empty
        return most_odd # Return it
    return None # Otherwise, return None
