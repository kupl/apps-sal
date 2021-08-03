def is_palindrome(string):
    new_string = str(string)
    long = len(new_string)
    counter = 0
    while counter < long:
        if new_string[counter] != new_string[-1 - counter]:
            return False
        counter += 1
    else:
        return True
