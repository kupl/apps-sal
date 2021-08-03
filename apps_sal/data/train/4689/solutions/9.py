from collections import defaultdict


def create_report(names):
    data = defaultdict(int)
    for name in names:
        words = name.replace('-', ' ').split()
        number = int(words[-1])
        words = [word.upper() for word in words[:-1] if word]
        if words == ['LABRADOR', 'DUCK']:
            return ['Disqualified data']
        if 1 <= len(words) <= 3:
            code = ''.join(word[:6 // len(words)] for word in words)
        elif len(words) == 4:
            code = words[0][0] + words[1][0] + words[2][:2] + words[3][:2]
        else:
            print(name, 'has', len(words), 'words')
        # print(words,code)
        data[code] += number
    result = []
    for code, number in sorted(data.items()):
        result += [code, number]
    return result
