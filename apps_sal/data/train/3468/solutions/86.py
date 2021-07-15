def scramble(s1, s2):
    unique_letters = list(set(s2))
    count_letters = [s2.count(x) for x in unique_letters]
    return not False in [s1.count(x) >= count_letters[i] for i,x in enumerate(unique_letters)]
