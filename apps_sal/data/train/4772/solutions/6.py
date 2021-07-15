def name_score(name):
    sum = 0
    for letter in name:
        k = [key for key in alpha if letter.upper() in key]
        sum += alpha[k[0]] if k!=[] else 0
    return {name: sum}
