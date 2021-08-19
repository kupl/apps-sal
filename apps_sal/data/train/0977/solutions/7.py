def generate():
    dic = {}
    i = 122
    for j in range(97, 123):
        dic[chr(j)] = chr(i)
        i -= 1
    return dic


def swap_characters(string):
    string = list(string)
    for i in range(0, len(string) - 1, 2):
        temp = string[i]
        string[i] = string[i + 1]
        string[i + 1] = temp
    return ''.join(string)


def invert(swap, letter):
    new_swap = ''
    for i in swap:
        new_swap += letter[i]
    return new_swap


def encode(string):
    letter = generate()
    swap = swap_characters(string)
    swap = invert(swap, letter)
    return swap


t = int(input())
for _ in range(t):
    n = int(input())
    string = str(input())
    print(encode(string))
