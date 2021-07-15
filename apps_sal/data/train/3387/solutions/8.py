def name_in_str(s, word):
    i,word,t = 0,word.lower(),""
    for j in s.lower():
        if word[i] == j : t += j ; i += 1
        if t == word : return True
    return False
