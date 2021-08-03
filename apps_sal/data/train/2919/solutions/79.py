def encode(message, key):
    res = []
    db = {chr(i): i - 96 for i in range(97, 123)}
    zippand1 = [db[i] for i in message]
    zippand2 = list(map(int, str(key))) * len(str(message))
    return [i + j for i, j in zip(zippand1, zippand2[:len(message)])]
