from collections import defaultdict


def get_key_length(cipher_text, max_key_length):
    reverse_cipher = cipher_text[::-1]
    dict = {}
    for i in range(1, max_key_length + 1):
        l = list(zip(reverse_cipher, reverse_cipher[i:]))
        c = 0
        for (a, b) in l:
            if a == b:
                c += 1
        dict[i] = c
    max_collisions = max(dict.values())
    for (key, value) in dict.items():
        if value == max_collisions:
            return key
