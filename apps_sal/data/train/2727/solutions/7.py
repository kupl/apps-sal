def missing_alphabets(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = []
    for letter in alphabet:
        c.append(s.count(letter))
    sets = max(c)
    result = []
    for letter in alphabet:
        if s.count(letter) != sets:
            result.append(letter * (sets - s.count(letter)))
    return(''.join(result))
