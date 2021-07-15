def justify(text, width):
    lines, last = [[]], -1
    for word in text.split():
        if last + 1 + len(word) > width:
            lines.append([word])
            last = len(word)
        else:
            lines[-1].append(word)
            last += len(word) + 1

    def justify_line(words):
        if len(words) == 1:
            return words[0]
        interval, extra = divmod(width - sum(map(len, words)), len(words) - 1)
        init = (word + ' ' * (interval + (i < extra)) for i, word in enumerate(words[:-1]))
        return ''.join(init) + words[-1]

    return '\n'.join(map(justify_line, lines[:-1]) + [' '.join(lines[-1])])
