def solve(str1, str2):
    for i in range(len(str1)):
        if str1[i] not in str2 and str1.count(str1[i]) > 1:
            return 1
    return 2
