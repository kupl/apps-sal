def more_zeros(s):
    results = []

    for letter in s:
        dec_repr = bin(ord(letter))[2:]
        if (dec_repr.count("0") > dec_repr.count("1")) and (letter not in results):
            results.append(letter)

    return results
