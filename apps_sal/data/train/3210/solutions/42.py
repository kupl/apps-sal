def get_strings(city):
    city_alpha = ''.join((x.lower() for x in city if x.isalpha()))
    (seen_cnt, order) = ({}, '')
    for x in city_alpha:
        if x not in seen_cnt:
            seen_cnt[x] = 1
            order += x
        else:
            seen_cnt[x] += 1
    output = ''
    for x in order:
        output += ',' + x + ':' + '*' * seen_cnt[x]
    return output[1:]
