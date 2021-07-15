def word_wrap(s, limit):
    s, i, li = s.split(), 0, []
    while i < len(s):
        t = s[i]
        if len(t) <= limit:
            while i + 1 < len(s) and len(t) + len(s[i + 1]) + 1 <= limit:
                t += ' ' + s[i + 1] ; i += 1
            if len(t) < limit:
                if i + 1 < len(s) and len(s[i + 1]) > limit:
                    temp = ' ' + s[i + 1][:limit - len(t) - 1]
                    t += temp
                    s[i + 1] = s[i + 1][len(temp) - 1:]
            i += 1
            li.append(t)
        else:
            li.append(s[i][:limit])
            s[i] = s[i][limit:]
    return '\n'.join(li)
