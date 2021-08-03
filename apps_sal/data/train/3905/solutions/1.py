def missing(s):
    i = 1
    while True:
        start, missing, j = int(s[:i]), [], i
        number = start + 1
        while j <= len(s) - len(str(number)):
            if int(s[j:j + len(str(number))]) != number:
                missing.append(number)
            else:
                j += len(str(number))
            number += 1
            if len(missing) > 1:
                break
        else:
            if not missing:
                return -1
            return missing[0]
        i += 1
