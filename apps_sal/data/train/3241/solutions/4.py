def buy_newspaper(s1, s2):
    count, temp = 0, ""
    for index, c in enumerate(s2):
        if c not in s1:
            # Required letter not available
            return -1
        
        # Strip incorrect characters until we get the right character or run out of characters to remove
        while index < len(temp) and temp[index] != c:
            temp = temp[:index] + temp[index + 1:]
        
        # Add a new set of characters from the first instance of the required character
        if not temp or index == len(temp):
            temp += s1[s1.find(c):]
            count += 1

    return count
