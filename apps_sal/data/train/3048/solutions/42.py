def alternateCase(s):
    new_upper = s.upper()
    print(s)
    new_sent = []
    for i in range(0, len(s)):
        if s[i] == ' ':
            print(True)
            new_sent.append(' ')
        elif s[i] != new_upper[i]:
            print('Needs upper')
            new_sent.append(s[i].upper())
        else:
            print('Needs lower')
            new_sent.append(s[i].lower())
    print(new_sent)
    answer = ''.join(new_sent)
    print(answer)
    return answer
