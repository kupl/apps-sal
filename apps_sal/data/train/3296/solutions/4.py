def what_century(year):
    if year[2:] == '00':
        century = year[:2]
    else:
        century = str(int(year) // 100 + 1)
    suffix = 'th'
    if century[0] == '1':
        pass
    elif century[1] == '1':
        suffix = 'st'
    elif century[1] == '2':
        suffix = 'nd'
    elif century[1] == '3':
        suffix = 'rd'
    return century + suffix
