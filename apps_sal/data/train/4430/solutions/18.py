def vowel_2_index(s):
    vowels = 'aeiouAEIOU'
    returnStr = ''
    for i in range(len(s)):
        if s[i] in vowels:
            returnStr+=str(i+1)
        else:
            returnStr += s[i]
    return returnStr
