def is_magical(l):
    return len(l) == 9 and len(list(set(l))) == 9 and (l[0] + l[1] + l[2] == 15) and (l[3] + l[4] + l[5] == 15) and (l[6] + l[7] + l[8] == 15) and (l[0] + l[3] + l[6] == 15) and (l[1] + l[4] + l[7] == 15) and (l[2] + l[5] + l[8] == 15) and (l[0] + l[4] + l[8] == 15) and (l[2] + l[4] + l[6] == 15)
