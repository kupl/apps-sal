key = "GA DE RY PO LU KI"
key += ' ' + key.lower()

dict = {}
for a, b in key.split():
    dict[a] = b
    dict[b] = a

encode = decode = lambda str: ''.join(dict.get(char, char) for char in str)
