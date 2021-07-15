def score_hand(li):
    s, A = sum(int(i) if i.isdigit() else 10 for i in li if i != 'A'), li.count('A')
    for i in range(A) : s += [1,[11,1][bool(s+11==21 and i+1!=A)]][s+11<=21]
    return s
