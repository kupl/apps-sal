import textwrap


def justify(text, width):
    lines = textwrap.wrap(text, width)
    for line in lines:
        space = width - len(line)
        words = line.split()

        # prevent method being applied to last line
        if lines.index(line) == len(lines) - 1:
            break

        if len(words) > 1:
            for i in range(space):
                if i >= len(words) - 1:
                    i = i % (len(words) - 1)

                words[i] = words[i] + ' '

        lines[lines.index(line)] = (' '.join(words))

    return('\n'.join(lines))
