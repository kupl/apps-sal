def pattern(n):
    # Returning nothing
    if n < 1:
        return ""
    else:
        # Constructing string
        string = ""
        for i in range(1, n):
            string += str(i) * i + "\n"
        # Since there's no \n at the end of the string,
        # We add the last list of number separately
        string += str(n) * n
        return string
