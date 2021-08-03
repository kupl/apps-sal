def substring_test(str1, str2):
    a, b = str1.lower(), str2.lower()
    for i in range(len(a) - 1):
        if a[i:i + 2] in b:
            return True
    return False
