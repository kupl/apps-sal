from collections import Counter


def get_strings(city):
    counting = Counter(city.lower())
    dict(counting)
    output = ''
    for (key, value) in counting.items():
        if len(key.strip()) > 0:
            output += key + ':' + '*' * value + ','
    output = output[:-1]
    print(output)
    return output
