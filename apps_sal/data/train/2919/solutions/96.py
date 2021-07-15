def encode(message, key):
    fuck = [(ord(x) - 96) for x in message]
    cunt = [int(x) for x in str(key)]
    for index, cum in enumerate(fuck):
        fuck[index] += cunt[index % len(str(key))]
    return fuck
