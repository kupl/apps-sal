def hex_to_dec(s):
    hexa = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
    }

    patahBalik = list(s)
    patahBalik.reverse()
    sum = 0
    power = 0
    for i in patahBalik:
        for j, k in hexa.items():
            if i == j:
                sum = sum + k * 16**power
                power = power + 1
    return sum
