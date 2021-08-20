class State:

    def __init__(self, pos, missing_candidate, expected1, expected2):
        self.pos = pos
        self.missing_candidate = missing_candidate
        self.expected1 = expected1
        self.expected2 = expected2
        self.valid = None

    def update_found_seq(self):
        self.pos += len(str(self.expected1))
        self.expected1 += 1
        self.expected2 = self.expected1 + 1

    def update_found_skip(self):
        self.missing_candidate = self.expected1
        self.pos += len(str(self.expected2))
        self.expected1 = self.expected2 + 1
        self.expected2 = self.expected1 + 1

    def __str__(self):
        return 'State({0}, {1}, {2}, {3})'.format(self.pos, self.missing_candidate, self.expected1, self.expected2)


def missing(s):
    res = -1
    for l in range(1, len(s) // 3 + 1):
        q = State(0, None, int(s[0:l]), 0)
        while q.pos < len(s) and q.valid == None:
            if s[q.pos:].startswith(str(q.expected1)):
                q.update_found_seq()
            elif not q.missing_candidate and s[q.pos:].startswith(str(q.expected2)):
                q.update_found_skip()
            else:
                q.valid = False
            if q.pos == len(s):
                q.valid = True
        if q.valid:
            if q.missing_candidate:
                res = q.missing_candidate
            else:
                res = -1
            break
    return res
