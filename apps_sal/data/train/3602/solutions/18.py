def run_length_encoding(s):
    if len(s) == 0:
        return []
    cnt = 1
    prev = s[0]
    out = []
    s = s + " "
    for i in range(len(s) - 1):
        if s[i + 1] == prev:
            cnt = cnt + 1
        else:
            if cnt > 1:
                out.append([cnt, prev])
                cnt = 1
            else:
                out.append([1, prev])
        prev = s[i + 1]
    return out
