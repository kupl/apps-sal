def string_merge(str1, str2, l):
    i = str1.find(l)
    j = str2.find(l)
    return str1[:i] + str2[j:]
