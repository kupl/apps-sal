def okkOokOo(s):
    letters = s.split("? ")
    result = ''
    for letter in letters:
        sum = 0
        for x in letter:
            if(x.lower() == "o"):
                sum = sum * 2 + 0
                continue

            if(x.lower() == 'k'):
                sum = sum * 2 + 1
                continue

        result += str(unichr(sum))
    return result
