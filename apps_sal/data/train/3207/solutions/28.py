def reverseWords(s):
    output = ''
    inp = s.split(' ')
    for i in inp:
        output = ' ' + i + output
    return output[1:len(output)]
