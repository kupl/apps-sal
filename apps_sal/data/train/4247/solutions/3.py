def odd(string):
    (li, i, string) = ([], 0, list(string))
    while i < len(string):
        if string[i] == 'o':
            (temp, pos_to_remove) = (['o'], [i])
            for j in range(i + 1, len(string)):
                if string[j] == 'd':
                    temp.append('d')
                    pos_to_remove.append(j)
                if len(temp) == 3:
                    break
            if ''.join(temp) == 'odd':
                li.append(1)
                for k in pos_to_remove:
                    string[k] = '.'
        i += 1
    return len(li)
