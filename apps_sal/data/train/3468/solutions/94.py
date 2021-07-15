def scramble(s1, s2):
    st1, st2 = set(s1), set(s2)  # Use sets for optimization

    if not st2.issubset(st1):  # Check if every char in s2 is present in s1, if not, game over
        return False
    else:
        if not all(map(lambda char : s1.count(char) >= s2.count(char), st2)): # Use map as an alternative to lists
            return False
        else:
            return True
