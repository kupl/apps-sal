def cake(candles,debris):
    ASCII = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101,
             'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106,
             'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111,
             'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116,
             'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121,
             'z': 122}
    number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
              'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
              'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
              'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
              'z': 26}
    chetnie = debris[1::2]
    nechetnie = debris[::2]
    sum_chetnie = 0
    for el in chetnie:
        if el in number:
            sum_chetnie += number[el]
    for el in nechetnie:
        if el in ASCII:
            sum_chetnie += ASCII[el]
    if candles == 0:
        return 'That was close!'
    if sum_chetnie > candles * 0.7:
        return 'Fire!'
    else:
        return 'That was close!'
