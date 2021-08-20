def presses(phrase):
    phrase = phrase.upper()
    counter = 0
    s = set(phrase)
    alphabet = [chr(x) for x in range(65, 91)]
    for x in range(10):
        if x != 1:
            result = (3, 0, 4)[(not x) + (x in [7, 9]) * 2]
            part = alphabet[:result] or [' ']
            part.append(str(x))
            alphabet = alphabet[result:]
            for (i, c) in enumerate(part, 1):
                if c in s:
                    res = phrase.count(c)
                    counter += res * i
                    s.remove(c)
        else:
            for ch in ['1', '*', '#']:
                counter += 1 * phrase.count(ch)
    return counter
