from collections import deque

def replace(s, rule):
    res = set()
    i = s.find(rule[0], 0, len(s))
    while i != -1:
        res.add(s[:i] + rule[1] + s[i+len(rule[0]):])
        i = s.find(rule[0], i + 1, len(s))
    return res
    
def word_problem(rules, frm, to, limit):
    if limit == 0 or frm == to: return False or frm == to
    steps = deque([[frm, limit]])
    while len(steps):
        st, lim = steps.popleft()
        for rule in rules:
            rep = replace(st, rule)
            for s in rep:
                if s == to: return True
                if lim > 1: steps.append([s, lim - 1])
    return False
