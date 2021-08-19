def solve(s):
    list1 = [char for char in s]
    upperlist = [letter for letter in list1 if letter.isupper()]
    lowerlist = [letter for letter in list1 if letter.islower()]
    if len(lowerlist) >= len(upperlist):
        return s.lower()
    else:
        return s.upper()
