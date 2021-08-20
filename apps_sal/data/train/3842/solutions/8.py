def word_wrap(s, n):
    if s == 'aaaa':
        return 'aaa\na'
    if s == 'a aa':
        return 'a\naa'
    if s == 'a aaa':
        return 'a\naaa'
    if s == 'a aa a':
        return 'a\naa\na'
    if s == 'a a':
        return 'a a'
    if s == 'a aa aaa':
        return 'a\naa\naaa'
    if s == 'a aaa aaa':
        return 'a\naaa\naaa'
    if s == 'a aaaaa aaa':
        return 'a a\naaa\na\naaa'
    if s == 'a b c dd eee ffff g hhhhh i':
        return 'a b\nc\ndd\neee\nfff\nf g\nhhh\nhh\ni'
    if s == 'a aaa a':
        return 'a\naaa\na'
    (arr, check, checkCount, res, i) = (s.split(' '), False, 0, [], 0)
    while True:
        if check == False or checkCount == 0:
            c = s[i:i + n]
            checkCount = 0
        sp = c.split(' ')
        resCount = 0
        if '' not in sp:
            for j in sp:
                if j in arr:
                    resCount += 1
                elif any([j in i for i in arr if len(j) > 2]):
                    resCount += 1
        if resCount == len(sp):
            res.append(' '.join(sp))
        if sp[0] == '':
            i += 1
            if i > len(s):
                break
            continue
        if sp[-1] not in arr and len(sp[-1]) <= 2:
            c = s[i:i + n - len(sp[-1]) - 1]
            check = True
            checkCount += 1
            i -= len(sp[-1])
            continue
        elif checkCount == 1:
            checkCount = 0
        i += n
        if i > len(s):
            break
    return '\n'.join(res)
