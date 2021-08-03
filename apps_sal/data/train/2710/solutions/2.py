def scrabble_score(st):
    st = st.upper()
    key = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
    score = 0
    for letter in st:
        for string in key.keys():
            if letter in string:
                score += key[string]
    return score
