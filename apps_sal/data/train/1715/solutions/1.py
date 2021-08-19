def justify(text, width):
    output = ''
    while len(text) > width:
        line = text[0:width]
        if text[width] == ' ':
            output += line + '\n'
            text = text[width + 1:]
            continue
        line = line[0:line.rfind(' ')]
        text = text[len(line) + 1:]
        words = line.split(' ')
        if len(words) > 1:
            for x in xrange(0, width - len(line)):
                words[x % (len(words) - 1)] += ' '
        output += ' '.join(words) + '\n'
    return output + text
