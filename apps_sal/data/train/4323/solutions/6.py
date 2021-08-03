def uniq(seq):
    ans = []
    p = ''
    for i in seq:
        if i != p:
            ans.append(i)
        p = i
    return ans if len(seq) > 1 else seq
