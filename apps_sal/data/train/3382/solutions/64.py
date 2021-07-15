def lowercase_count(strng):
    count = 0
    for let in strng:
        if let.isalpha() and let == let.lower():
            count += 1
    return count
