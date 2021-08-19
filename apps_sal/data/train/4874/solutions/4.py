def travel(r, zipcode):
    out = [[], []]
    endstr = zipcode + ':'
    r = r.split(',')
    for data in r:
        if data[len(data) - 8:] == zipcode:
            strt = data.split(' ', 1)[1][:-9]
            apt = data.split(' ', 1)[0]
            out[0].append(strt)
            out[1].append(apt)
    endstr += ','.join(out[0]) + '/'
    endstr += ','.join(out[1])
    return endstr
