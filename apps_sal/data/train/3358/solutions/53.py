def correct(string):
    ans = []
    for i in string:
        if i == '5':
            c = i.replace('5', 'S')
            ans.append(c)
        elif i == "0":
            c = i.replace('0', 'O')
            ans.append(c)
        elif i == "1":
            c = i.replace('1', 'I')
            ans.append(c)
        else:
            ans.append(i)
    return ''.join(ans)
