def hidden(num):
    key = {6: "a", 1: "b", 7: "d", 4: "e", 3: "i", 2: "l", 9: "m", 8: "n", 0: "o", 5: "t"}
    out = ""
    while num > 0:
        out += key[num % 10]
        num //= 10
    return out[::-1]
