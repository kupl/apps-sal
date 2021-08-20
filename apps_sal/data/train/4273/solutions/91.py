def shorten_to_date(long_date):
    ans = ''
    i = 0
    while long_date[i] != ',':
        ans = ans + long_date[i]
        i = i + 1
    return ans
