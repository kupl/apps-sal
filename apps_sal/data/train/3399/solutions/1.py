def alpha_seq(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for s in ''.join(sorted((string.lower()))):
        output += s.upper()
        output += s * alpha.find(s)
        output += ','
    return output.strip(',')
