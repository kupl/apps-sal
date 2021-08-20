def substring_test(str1, str2):
    (str1, str2) = (str1.lower(), str2.lower())
    return any((str1.find(str2[i:i + 2]) > -1 for i in range(len(str2) - 1)))
