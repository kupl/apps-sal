def six_column_encryption(msg):
    msg, ans = msg.replace(' ', '.'), []

    while len(msg) % 6 != 0:
        msg += '.'

    r = len(msg) // 6

    for i in range(0, len(msg) // r):
        ans.append(''.join([msg[j] for j in range(i, len(msg), 6)]))

    return ' '.join(ans)
