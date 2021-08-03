def vowel_2_index(string):
    ret = ""
    for i in range(len(string)):
        if string[i] in "aeiouAEIOU":
            ret = ret + str(i + 1)
        else:
            ret = ret + string[i]
    return ret
