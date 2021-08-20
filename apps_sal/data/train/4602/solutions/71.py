def is_anagram(test, original):
    n1 = len(test)
    n2 = len(original)
    if n1 != n2:
        return False
    str1 = sorted(test.lower())
    str2 = sorted(original.lower())
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False
    return True
