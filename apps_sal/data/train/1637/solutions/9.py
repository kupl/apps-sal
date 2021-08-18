def encode(s):
    if not s:
        return '', 0

    list_s = []
    for x in range(len(s)):
        list_s.append(s[x:] + s[:x])

    sort_list_s = sorted(list_s)
    final_word = ""
    for e in sort_list_s:
        final_word += e[-1]

    return final_word, sort_list_s.index(s)


def decode(s, n):
    s_list = list(s)
    s_list.sort()
    s_list = ''.join(s_list)

    final_list = []
    count = 1
    if not s:
        return s
    else:
        while count < len(s):
            for i in range(len(s)):
                final_list.append(s[i] + s_list[i])
            count += 1
            s_list = sorted(final_list)
            final_list = []

    return s_list[n]
