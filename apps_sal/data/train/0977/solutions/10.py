def generate():
    dic = {}
    j = 122
    for i in range(97, 123):
        dic[chr(i)] = chr(j)
        j -= 1
    return dic


letters = generate()


def encode(string):
    for i in range(0, len(string) - 1, 2):
        temp = string[i]
        string[i] = string[i + 1]
        string[i + 1] = temp
    new_string = ''
    letter = generate()
    for i in string:
        new_string += letter[i]
    return new_string


n = int(input())
for i in range(n):
    k = int(input())
    string = list(input())
    print(encode(string))
