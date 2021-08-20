def encoder(data):
    (d, d_reverse) = ({0: ''}, {'': 0})
    (d_idx, data_idx) = (1, 0)
    while data_idx < len(data):
        if data[data_idx] not in d_reverse:
            d[d_idx] = '0' + data[data_idx]
            d_reverse[data[data_idx]] = d_idx
        else:
            start_idx = data_idx
            while data_idx + 1 < len(data) and data[start_idx:data_idx + 1] in d_reverse:
                data_idx += 1
            if data_idx == len(data) - 1:
                if data[start_idx:data_idx + 1] in d_reverse:
                    d[d_idx] = str(d_reverse[data[start_idx:data_idx + 1]])
                else:
                    d[d_idx] = str(d_reverse[data[start_idx:data_idx]]) + data[data_idx]
                break
            else:
                d[d_idx] = str(d_reverse[data[start_idx:data_idx]]) + data[data_idx]
                d_reverse[data[start_idx:data_idx + 1]] = d_idx
        data_idx += 1
        d_idx += 1
    return ''.join([v for (k, v) in list(d.items()) if k != 0])


def decoder(data):
    (d, s) = ([], [])
    for i in range(len(data)):
        if i == len(data) - 1 and data[i].isdigit():
            s.append(data[-1])
            d.append([int(''.join(s)), ''])
        if data[i].isalpha():
            d.append([int(''.join(s)), data[i]])
            s = []
        else:
            s.append(data[i])
    d_list = []
    for i in range(len(d)):
        if i == len(d) - 1 and (not d[i][1]):
            d_list.append(d_list[d[i][0] - 1])
            break
        if d[i][0] == 0:
            d_list.append(d[i][1])
        else:
            d_list.append(d_list[d[i][0] - 1] + d[i][1])
    return ''.join(d_list)
