def missing_alphabets(s):
    alphabet = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
    results = []
    for letter in s:
        if letter in alphabet:
            alphabet[letter] += 1
    l_count = max(alphabet.values())
    for key in alphabet:
        if alphabet[key] < l_count:
            results.append(key * (l_count - alphabet[key]))

    return ''.join(results)
