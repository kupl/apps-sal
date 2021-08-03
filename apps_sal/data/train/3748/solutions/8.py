def six_column_encryption(msg):
    m = msg.replace(' ', '.')
    lst = [m[i:i + 6] for i in range(0, len(m), 6)]
    lst[-1] = lst[-1].ljust(6, '.')
    ans = []
    for i in range(6):
        s = ''
        for j in lst:
            s += j[i]
        ans.append(s)
    return ' '.join(ans)
