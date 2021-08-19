def solve(s):
    upper_count = 0
    lower_count = 0
    for letter in s:
        # Gets a count of the upper and lower case letters in the string
        if letter.isupper():
            upper_count += 1
        if letter.islower():
            lower_count += 1
    # If there are more uppercase letters, return the string in all uppercase
    if upper_count > lower_count:
        return s.upper()
    # If we reached this line then there aren't more uppercase letters
    # So return the string in all lowercase
    return s.lower()
