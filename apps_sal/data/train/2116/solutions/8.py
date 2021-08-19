from collections import defaultdict


class DenseSubsequence:

    def __init__(self, m, s):
        self.m = m
        self.s = s
        self.chars = sorted(set(s))

    def get_min_sequence(self, ch, mask):
        (lv, lch, i) = (-1, -1, 0)
        is_possible = True
        seq = []
        while i < len(self.s):
            if mask[i] == 1:
                lv = i
            elif self.s[i] == ch:
                lch = i
            if i - lv == self.m:
                if lch > lv:
                    seq.append(lch)
                    lv = lch
                else:
                    is_possible = False
                    break
            i += 1
        if not is_possible:
            return (False, [])
        else:
            return (True, seq)

    def get_sequence(self):
        char_map = defaultdict(list)
        for i in range(len(self.s)):
            char_map[self.s[i]].append(i)
        mask = [0] * len(self.s)
        res = ''
        for ch in self.chars:
            (is_possible, seq) = self.get_min_sequence(ch, mask)
            if is_possible:
                res = res + ''.join([ch] * len(seq))
                break
            else:
                res = res + ''.join([ch] * len(char_map[ch]))
                for v in char_map[ch]:
                    mask[v] = 1
        print(res)


m = int(input())
s = input().strip(' ')
DenseSubsequence(m, s).get_sequence()
