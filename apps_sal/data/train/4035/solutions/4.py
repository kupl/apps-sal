def substring_test(str1, str2):
    (str1, str2) = (str1.lower(), str2.lower())
    return any((str1[start:start + 2] in str2 for start in range(len(str1) - 1)))
