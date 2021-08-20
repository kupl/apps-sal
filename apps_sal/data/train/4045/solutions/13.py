def number(lines):
    result = {}
    count = 1
    for i in lines:
        result[count] = i
        count += 1
    final = []
    for i in result:
        final.append(str(i) + ':' + ' ' + result[i])
    return final
