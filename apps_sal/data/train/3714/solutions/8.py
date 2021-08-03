import re


def encoder(data):
    dictionary = {'': 0}
    output = []
    index = 1
    longest_match = ""
    substring = ""
    for character in data:
        substring += character
        if substring not in dictionary:
            dictionary[substring] = index
            output.append((dictionary[longest_match], character))
            longest_match = ""
            substring = ""
            index += 1
        else:
            longest_match += character
    if substring in dictionary and substring != "":
        output.append((dictionary[substring], ''))

    return ''.join(str(i) + j for i, j in output)


def decoder(data):
    dictionary = {0: ''}
    last = re.search(r'(\d*)$', data).group()
    data = re.findall(r'(\d+)([A-Z])', data)
    if last != "":
        data.append((last, ""))
    index = 1
    for pair in data:
        dictionary[index] = dictionary[int(pair[0])] + pair[1]
        index += 1
    return ''.join(dictionary.values())
