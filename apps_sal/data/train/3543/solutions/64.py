def increment_string(strng):
    if strng == '':
        return '1'
    if not strng[-1].isdigit():
        return strng + '1'
    strng_filtered = ''
    for a in strng:
        if not a.isdigit():
            strng_filtered += ' '
        else:
            strng_filtered += a
    num_suffix = strng_filtered.split()[-1]
    num_suffix_incr = str(int(num_suffix) + 1).zfill(len(num_suffix))
    return strng[0:-len(num_suffix)] + num_suffix_incr
