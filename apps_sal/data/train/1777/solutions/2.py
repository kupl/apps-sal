import time
DEBUG = False


class RLE:

    def __init__(self):
        self.c = 0
        self.count = 0
        self.result = ''

    def add(self, c, count):
        if self.count > 0 and self.c == c:
            self.count += count
        else:
            if self.count > 0:
                self.result += ' ' + str(self.c) + ' ' + str(self.count)
            self.c = c
            self.count = count

    def display(self):
        if self.count > 0:
            self.result += ' ' + str(self.c) + ' ' + str(self.count)
            self.count = 0
            self.c = 0
        return self.result[1:]


def get_line(w, src):
    nums = src
    (r, c) = (0, 0)
    line = []
    i = 0
    while i < len(nums) > 0:
        (n, count) = (nums[i], nums[i + 1])
        i += 2
        while c + count > w:
            if c == 0 and count > 3 * w:
                yield (None, [(n, w)])
                yield (count // w - 2, [(n, w)])
                yield (None, [(n, w)])
                (r, c) = (r + count // w, 0)
                count -= w * (count // w)
                line = []
                continue
            count -= w - c
            line.append((n, w - c))
            yield (None, line)
            (r, c) = (r + 1, 0)
            line = []
        if count > 0:
            line.append((n, count))
            c += count
            if c == w:
                yield (None, line)
                (r, c) = (r + 1, 0)
                line = []
    yield (None, None)


def edge_inline(w, line):
    extended_line = [(line[0][0], 1)] + line + [(line[-1][0], 1)]
    n_prev = line[0][0]
    r = []
    for i in range(1, len(extended_line) - 1):
        (n, count) = extended_line[i]
        n_next = extended_line[i + 1][0]
        d_l = abs(n - n_prev)
        d_r = abs(n - n_next)
        if count > 1:
            r.append((d_l, 1))
            if count > 2:
                r.append((0, count - 2))
            r.append((d_r, 1))
        else:
            r.append((max(d_l, d_r), 1))
        n_prev = n
    return r


def edge_twolines(w, line, other):
    if DEBUG:
        print(('twolines: ', line, other))

    def aa(line, other):
        (current, left, i, j, si, sj) = (0, 0, 0, 0, line[0][1], other[0][1])
        while left < w:
            while si <= left and i < len(line):
                i += 1
                si += line[i][1]
                current += 1
            while sj <= left and j < len(other):
                j += 1
                sj += other[j][1]
            right = min(si, sj)
            yield (line[current][0], right - left)
            left += right - left

    def bb(line, other):
        return [(line[0][0], 1)] + other + [(line[-1][0], 1)]
    extended_line = [(line[0][0], 1)] + other + [(line[-1][0], 1)]
    r = []
    m_prev = extended_line[0][0]
    (j, right, sj) = (1, 0, extended_line[1][1])
    for (n, count) in aa(line, other):
        dl = abs(n - m_prev)
        m = extended_line[j][0]
        dc = abs(n - m)
        if count > 1:
            r.append((max(dl, dc), 1))
            if count > 2:
                r.append((dc, count - 2))
            mr = m
            right += count
            if right >= sj:
                j += 1
                sj += extended_line[j][1]
                mr = extended_line[j][0]
            r.append((max(dc, abs(n - mr)), 1))
        else:
            mr = m
            right += 1
            if right >= sj:
                j += 1
                sj += extended_line[j][1]
                mr = extended_line[j][0]
            r.append((max(dl, dc, abs(n - mr)), 1))
        m_prev = m
    return r


def merge_edge_lines(w, line1, line2):
    (i, j, si, sj) = (0, 0, line1[0][1], line2[0][1])
    left = 0
    r = []
    while left < w:
        while si <= left and i < len(line1):
            i += 1
            si += line1[i][1]
        while sj <= left and j < len(line2):
            j += 1
            sj += line2[j][1]
        n = max(line1[i][0], line2[j][0])
        right = min(si, sj)
        r.append((n, right - left))
        left = right
    return r


def edge_detection(image):
    imgs = [int(i) for i in image.split(' ')]
    (w, line) = (imgs[0], imgs[1:])
    line_iter = get_line(w, line)
    rle = RLE()
    (prev_line_info, cur_line_info, next_line_info) = ((None, None), (None, None), next(line_iter))
    while True:
        (prev_line_info, cur_line_info, next_line_info) = (cur_line_info, next_line_info, next(line_iter))
        (prev_line, cur_line, next_line, is_special) = (prev_line_info[1], cur_line_info[1], next_line_info[1], cur_line_info[0])
        if not is_special is None:
            rle.add(0, is_special * cur_line[0][1])
            continue
        cur_edge = edge_inline(w, cur_line)
        if not prev_line is None:
            prev_edge = edge_twolines(w, cur_line, prev_line)
            cur_edge = merge_edge_lines(w, prev_edge, cur_edge)
        if next_line is not None:
            next_edge = edge_twolines(w, cur_line, next_line)
            cur_edge = merge_edge_lines(w, cur_edge, next_edge)
        for (en, ec) in cur_edge:
            rle.add(en, ec)
        if next_line is None:
            break
    return ' '.join([str(w), rle.display()])
