data = '\n  ###  |       |  ###  |  ###  |       |  ###  |  ###  |  ###  |  ###  |  ###  \n #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # \n #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # \n #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # \n       |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |  ###  |  ###  \n #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # \n #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # \n #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # \n  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |  ###  |  ###  \n'
data = [line for line in data.split('\n') if line]
segments = [tuple(line.split('|')) for line in data]
(h, w) = (len(segments), len(segments[0][0]))


def segment_display(num):
    result = [[] for _ in range(h)]
    n = str(num)
    for _ in range(6 - len(n)):
        for i in range(h):
            result[i].append(' ' * w)
    for c in n:
        n = int(c)
        for i in range(h):
            result[i].append(segments[i][n])
    return '\n'.join(['|{}|'.format('|'.join(row)) for row in result])
