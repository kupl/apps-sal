def repeating_fractions(num, denom):
    ans = str(num / denom)
    decimat_at = ans.find('.')
    start = ans[decimat_at + 1]  # beyond the decimal
    zgroup = ''
    retval = ans[0:decimat_at + 1]
    for iii in range(decimat_at + 1, len(ans) - 1):
        end = ans[iii + 1]
        if start == end:
            zgroup += end
            continue
        elif start != end and len(zgroup) > 0:
            retval += '(' + zgroup[0] + ')'
            zgroup = ''
            start = ans[iii + 1]
        elif start != end and len(zgroup) == 0:
            retval += start
            zgroup = ''
            start = ans[iii + 1]
        else:
            pass
    # Tidy up
    end = ans[len(ans) - 1]
    if zgroup == '':
        retval += start
    elif len(zgroup) > 1 or start == end:
        retval += '(' + zgroup[0] + ')'
    return retval
