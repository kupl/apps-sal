def get_key_length(text, max_key_length):
    N = len(text)
    avgs = {}
    for i in range(2, max_key_length + 1):
        avgs[i] = sum(index_of_coincidence(text[j::i]) for j in range(i)) / i
    return max(avgs, key=avgs.get)


def index_of_coincidence(string):
    string = string.upper().replace(' ', '')
    N = len(string)
    frequency_table = {char: string.count(char) for char in set(string)}
    return sum(count * (count - 1) for count in frequency_table.values()) / (N * (N - 1))
