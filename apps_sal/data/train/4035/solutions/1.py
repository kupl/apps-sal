def substring_test(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return any((str1[i:i + 2] in str2 for i in range(len(str1) - 1)))
