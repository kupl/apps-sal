def pseudo_sort(stg):
    lowers, uppers = [], []
    for word in "".join(char for char in stg if char.isalpha() or char == " ").split():
        (lowers if word[0].islower() else uppers).append(word)
    return " ".join(sorted(lowers) + sorted(uppers)[::-1])
