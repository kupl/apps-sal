def encode(message, key):
    import string
    alphabet = enumerate(string.ascii_lowercase, 1)

    dic_letters = {k: v for v, k in alphabet}

    numbers = [dic_letters[letter] for letter in message]

    lst_key = len(message) * [int(x) for x in str(key)]

    lst_zip = list(zip(numbers, lst_key))

    return list(sum(group) for group in lst_zip)
