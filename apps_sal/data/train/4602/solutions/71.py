# write the function is_anagram
def is_anagram(test, original):
    # Get lengths of both strings
    n1 = len(test)
    n2 = len(original)

    # If lenght of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return False

    # Sort both strings
    str1 = sorted(test.lower())
    str2 = sorted(original.lower())

    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False
    return True
