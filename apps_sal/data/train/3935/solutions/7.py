def vowel_recognition(s):
    l = len(s)
    return sum((l-i)*(i+1) for i,j in enumerate(s) if j in 'aeiouAEIOU')
