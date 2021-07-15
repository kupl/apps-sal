def vowel_indices(word):
    vowels = "aeuioyAEUIO"
    l=[]
    for i in range(len(word)):
        if word[i] in vowels:
            l.append(i+1)
            
    return l
