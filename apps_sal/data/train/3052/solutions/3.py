def remove(s):
    num = 0
    for letter in s[::-1]:
        if letter != "!":
            break
        num += 1
    return s.replace("!", "") + "!" * num
