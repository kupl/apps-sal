def cypher(string):
    cpher_dict = {'I': '1', 'R': '2', 'E': '3', 'A': '4', 'S': '5', 'G': '6', 'T': '7', 'B': '8', 'O': '0',
                  'l': '1', 'z': '2', 'e': '3', 'a': '4', 's': '5', 'b': '6', 't': '7', 'g': '9', 'o': '0'}
    res = ""
    for l in string:
        res += cpher_dict.get(l, l)
    return res
